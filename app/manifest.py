"""SQLite ledger of what is indexed: doc_id -> content version (hash).
This is what makes sync idempotent: unchanged content is skipped, changed content
is re-embedded, and anything missing from the source is deleted."""
import sqlite3, threading, time
from pathlib import Path
from .config import settings


class Manifest:
    def __init__(self, path: str):
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(path, check_same_thread=False)
        self.lock = threading.Lock()
        with self.lock:
            self.conn.execute(
                """CREATE TABLE IF NOT EXISTS docs(
                    doc_id TEXT PRIMARY KEY, source_type TEXT, version TEXT,
                    chunk_count INTEGER, title TEXT, updated_at REAL)"""
            )
            self.conn.execute("CREATE INDEX IF NOT EXISTS idx_type ON docs(source_type)")
            self.conn.commit()

    def get_version(self, doc_id: str):
        with self.lock:
            r = self.conn.execute("SELECT version FROM docs WHERE doc_id=?", (doc_id,)).fetchone()
        return r[0] if r else None

    def upsert(self, doc_id, source_type, version, chunk_count, title=""):
        with self.lock:
            self.conn.execute(
                "INSERT OR REPLACE INTO docs VALUES(?,?,?,?,?,?)",
                (doc_id, source_type, version, chunk_count, title, time.time()),
            )
            self.conn.commit()

    def delete(self, doc_id: str):
        with self.lock:
            self.conn.execute("DELETE FROM docs WHERE doc_id=?", (doc_id,))
            self.conn.commit()

    def ids_with_prefix(self, prefix: str) -> set[str]:
        with self.lock:
            rows = self.conn.execute(
                "SELECT doc_id FROM docs WHERE substr(doc_id,1,?)=?", (len(prefix), prefix)
            ).fetchall()
        return {r[0] for r in rows}

    def list(self, source_type: str | None = None, limit: int = 500):
        q = "SELECT doc_id, source_type, chunk_count, title, updated_at FROM docs"
        args: tuple = ()
        if source_type:
            q += " WHERE source_type=?"; args = (source_type,)
        q += " ORDER BY updated_at DESC LIMIT ?"
        with self.lock:
            rows = self.conn.execute(q, args + (limit,)).fetchall()
        return [dict(doc_id=r[0], source_type=r[1], chunks=r[2], title=r[3], updated_at=r[4]) for r in rows]

    def stats(self):
        with self.lock:
            rows = self.conn.execute(
                "SELECT source_type, COUNT(*), SUM(chunk_count) FROM docs GROUP BY source_type"
            ).fetchall()
        return {r[0]: {"documents": r[1], "chunks": r[2]} for r in rows}


manifest = Manifest(settings.manifest_path)
