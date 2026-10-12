"""SQL -> knowledge base sync.

Each row = one document (doc_id = sql:<source>:<pk>). A row's version is the hash of its
rendered content, so:
  * new row        -> embedded + inserted
  * changed row    -> re-embedded, old chunks removed
  * unchanged row  -> skipped (no embedding cost)
  * deleted row    -> removed from the vector store
Two triggers: scheduled polling (always on) and Postgres LISTEN/NOTIFY (optional, instant)."""
import hashlib, json, logging, select, threading, time
from dataclasses import dataclass, field
from pathlib import Path

import yaml
from sqlalchemy import create_engine, text

from .chunking import chunk_sections
from .config import settings
from .ingest import Doc, index_documents, remove_doc
from .manifest import manifest

log = logging.getLogger("sql_sync")
BATCH = 64


@dataclass
class SQLSource:
    name: str
    primary_key: str
    table: str | None = None
    query: str | None = None
    text_columns: list[str] = field(default_factory=list)
    metadata_columns: list[str] = field(default_factory=list)
    interval_seconds: int = 60
    _lock: threading.Lock = field(default_factory=threading.Lock, repr=False)

    @property
    def select_sql(self) -> str:
        return self.query if self.query else f"SELECT * FROM {self.table}"

    @property
    def prefix(self) -> str:
        return f"sql:{self.name}:"


def table_key(name: str | None) -> str:
    """'[dbo].[Customers]' / 'dbo.customers' -> 'customers' (matches what the triggers send)."""
    return (name or "").split(".")[-1].strip("[]\" `").lower()


def load_sources() -> list[SQLSource]:
    if not settings.database_url or not Path(settings.sql_sources_file).exists():
        return []
    cfg = yaml.safe_load(Path(settings.sql_sources_file).read_text()) or {}
    return [SQLSource(**s) for s in cfg.get("sources", [])]


def get_source(name: str) -> SQLSource | None:
    return next((s for s in load_sources() if s.name == name), None)


_engine = create_engine(settings.database_url, pool_pre_ping=True) if settings.database_url else None

_PM_RAG_TOOL_SQL = """
    SELECT t.Id, t.ProjectName, t.Description, t.Level, l.Name AS LevelName
    FROM dbo.PMRagTool t
    LEFT JOIN dbo.PMRagToolLevel l ON t.Level = l.Id
"""


def fetch_pm_rag_tools(project_name: str | None = None, limit: int = 1000) -> list[dict]:
    """Live rows from dbo.PMRagTool (for UI preview, not the vector index)."""
    if _engine is None:
        return []
    limit = max(1, min(int(limit), 5000))
    sql = _PM_RAG_TOOL_SQL.strip()
    params: dict = {}
    if project_name:
        sql += " WHERE t.ProjectName = :project_name"
        params["project_name"] = project_name
    sql += " ORDER BY t.Id"
    if _engine.dialect.name == "mssql":
        sql = sql.replace("SELECT t.Id", f"SELECT TOP {limit} t.Id", 1)
    else:
        sql += f" LIMIT {limit}"
    with _engine.connect() as conn:
        rows = conn.execute(text(sql), params).mappings().all()
    return [_json_safe_row(dict(r)) for r in rows]


def preview_source_rows(source_name: str, limit: int = 500) -> list[dict]:
    """SELECT * (or custom query) for a configured sql_sources entry."""
    src = get_source(source_name)
    if src is None or _engine is None:
        return []
    limit = max(1, min(int(limit), 5000))
    inner = src.select_sql.strip().rstrip(";")
    if _engine.dialect.name == "mssql":
        sql = f"SELECT TOP {limit} * FROM ({inner}) AS _preview"
    else:
        sql = f"SELECT * FROM ({inner}) AS _preview LIMIT {limit}"
    with _engine.connect() as conn:
        rows = conn.execute(text(sql)).mappings().all()
    return [_json_safe_row(dict(r)) for r in rows]


def _json_safe_row(row: dict) -> dict:
    out = {}
    for k, v in row.items():
        if hasattr(v, "isoformat"):
            out[k] = v.isoformat()
        elif isinstance(v, (bytes, bytearray)):
            out[k] = v.decode("utf-8", errors="replace")
        else:
            out[k] = v
    return out


def _render(src: SQLSource, row: dict) -> tuple[str, dict]:
    cols = src.text_columns or list(row.keys())
    body = " | ".join(f"{c}: {row[c]}" for c in cols if row.get(c) not in (None, ""))
    meta = {"table": src.table or src.name, "pk": str(row[src.primary_key])}
    for c in src.metadata_columns:
        if c in row and row[c] is not None:
            meta[c] = str(row[c])
    return f"[{src.name}] {body}", meta


def _row_to_doc(src: SQLSource, row: dict) -> tuple[str, str, Doc]:
    pk = str(row[src.primary_key])
    body, meta = _render(src, row)
    version = hashlib.sha256((body + json.dumps(meta, sort_keys=True)).encode()).hexdigest()
    doc_id = f"{src.prefix}{pk}"
    return doc_id, version, Doc(doc_id, "sql", version, chunk_sections([(body, meta)]), title=f"{src.name}#{pk}")


def sync_source(src: SQLSource) -> dict:
    """Full reconciliation of one source. Cheap when nothing changed (one SELECT + hashing)."""
    if _engine is None:
        return {}
    if not src._lock.acquire(blocking=False):
        return {"source": src.name, "status": "already running"}
    try:
        t0 = time.time()
        seen: set[str] = set()
        pending: list[Doc] = []
        stats = {"source": src.name, "indexed": 0, "unchanged": 0, "deleted": 0}

        def flush():
            if pending:
                index_documents(pending)
                stats["indexed"] += len(pending)
                pending.clear()

        with _engine.connect().execution_options(stream_results=True) as conn:
            for row in conn.execute(text(src.select_sql)).mappings():
                doc_id, version, doc = _row_to_doc(src, dict(row))
                seen.add(doc_id)
                if manifest.get_version(doc_id) == version:
                    stats["unchanged"] += 1
                    continue
                pending.append(doc)
                if len(pending) >= BATCH:
                    flush()
        flush()

        # Deletions: only reached if the full SELECT succeeded (an exception skips this).
        for doc_id in manifest.ids_with_prefix(src.prefix) - seen:
            remove_doc(doc_id)
            stats["deleted"] += 1

        stats["seconds"] = round(time.time() - t0, 2)
        if stats["indexed"] or stats["deleted"]:
            log.info("sql sync %s", stats)
        return stats
    except Exception:
        log.exception("sql sync failed for %s", src.name)
        return {"source": src.name, "status": "error"}
    finally:
        src._lock.release()


def sync_row(src: SQLSource, pk: str, op: str):
    """Single-row fast path used by realtime notifications."""
    if src.query:                      # custom/joined query: can't address one row safely
        return sync_source(src)
    doc_id = f"{src.prefix}{pk}"
    if op == "DELETE":
        return remove_doc(doc_id)
    with _engine.connect() as conn:
        row = conn.execute(text(f"SELECT * FROM {src.table} WHERE {src.primary_key} = :pk"), {"pk": pk}).mappings().first()
    if row is None:
        return remove_doc(doc_id)
    _, version, doc = _row_to_doc(src, dict(row))
    if manifest.get_version(doc_id) != version:
        index_documents([doc])
        log.info("realtime indexed %s", doc_id)


def listen_forever(sources: list[SQLSource]):
    """Postgres LISTEN/NOTIFY: applies row changes within ~a second. Requires sql/postgres_triggers.sql."""
    import psycopg2
    by_table = {table_key(s.table): s for s in sources if s.table}
    dsn = settings.database_url.replace("+psycopg2", "")
    while True:
        try:
            conn = psycopg2.connect(dsn)
            conn.autocommit = True
            conn.cursor().execute("LISTEN rag_changes;")
            log.info("listening for realtime Postgres changes")
            while True:
                if not select.select([conn], [], [], 30)[0]:
                    continue
                conn.poll()
                while conn.notifies:
                    payload = json.loads(conn.notifies.pop(0).payload)
                    src = by_table.get(table_key(payload["table"]))
                    if src:
                        try:
                            sync_row(src, payload["pk"], payload["op"])
                        except Exception:
                            log.exception("realtime sync failed %s", payload)
        except Exception:
            log.exception("listener dropped; reconnecting in 5s (polling still keeps data fresh)")
            time.sleep(5)


def outbox_worker(sources: list[SQLSource], interval: float = 2.0):
    """Near-real-time sync for SQL Server (and MySQL etc.). Triggers insert (table, pk, op) rows
    into the outbox table (see sql/outbox_sqlserver.sql); this worker drains it every ~2s,
    de-duplicates, and re-indexes only the rows that changed."""
    by_table = {table_key(s.table): s for s in sources if s.table}
    T = settings.outbox_table
    top = f"SELECT TOP 500 id, table_name, pk, op FROM {T} ORDER BY id" if _engine.dialect.name == "mssql" \
        else f"SELECT id, table_name, pk, op FROM {T} ORDER BY id LIMIT 500"
    log.info("outbox worker started (%s)", T)
    while True:
        try:
            with _engine.connect() as conn:
                rows = conn.execute(text(top)).fetchall()
            if rows:
                latest: dict[tuple[str, str], str] = {}      # collapse repeated changes to the same row
                for r in rows:
                    latest[(table_key(r.table_name), str(r.pk))] = r.op
                full_resync: set[str] = set()
                for (tbl, pk), op in latest.items():
                    src = by_table.get(tbl)
                    if not src:
                        continue
                    if src.query:
                        full_resync.add(src.name)
                        continue
                    try:
                        sync_row(src, pk, op)
                    except Exception:
                        log.exception("outbox row failed %s %s", tbl, pk)
                for s in sources:
                    if s.name in full_resync:
                        sync_source(s)
                with _engine.begin() as conn:
                    conn.execute(text(f"DELETE FROM {T} WHERE id <= :m"), {"m": rows[-1].id})
                continue            # more may be waiting; don't sleep
        except Exception:
            log.exception("outbox worker error")
        time.sleep(interval)
