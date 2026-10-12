# RAG Knowledge Base

Unified knowledge base over **uploaded documents** (PDF, CSV, DOCX, TXT, MD) and **SQL Server rows**, with OpenAI embeddings and chat. Vectors live in **Qdrant**; a local **SQLite manifest** tracks document versions for cheap deduplication.

## Features

- **Files**: `POST /upload`, plus a watchdog on `data/files/`
- **SQL**: tables or custom queries in `sql_sources.yaml` — each row becomes one searchable document
- **Web UI** (`static/index.html`): live SQL table view, ingest button, Q&A over **files + SQL** or either alone
- **Sync**: polling per source + optional SQL Server outbox triggers for near-real-time updates
- **Startup**: background SQL sync when the API starts (if `DATABASE_URL` is set)

## Project layout

```
app/
  main.py          # FastAPI app, routes, scheduler
  config.py        # Settings from .env
  ingest.py        # index_documents() — shared path for files and SQL
  sql_sync.py      # SQL loaders, sync, outbox worker, live preview queries
  rag.py           # retrieve + OpenAI chat with citations
  vectorstore.py   # Qdrant client
  manifest.py      # SQLite doc_id → version
  loaders.py       # PDF / DOCX / CSV / text
  chunking.py      # Text chunking
  embeddings.py    # OpenAI (or local) embeddings
  watcher.py       # Folder watcher for data/files/
data/
  files/           # Uploaded / dropped files (indexed as file:…)
  manifest.db      # Local index state (gitignored; recreated on sync)
sql/
  outbox_sqlserver.sql   # Outbox table + trigger template
  postgres_triggers.sql  # Optional Postgres LISTEN/NOTIFY
static/
  index.html       # Simple dashboard
sql_sources.yaml   # Which SQL tables/queries to embed
.env.example       # Copy to .env (never commit .env)
docker-compose.yml # Local Qdrant
requirements.txt
```

## Architecture

```
 SOURCES                        INGESTION / SYNC                         STORAGE            SERVING
┌───────────────────┐
│ Upload API        │──┐
│ POST /upload      │  │     ┌─────────────────────────────┐
└───────────────────┘  ├───▶ │ Loaders (pdf/docx/csv/txt)  │
┌───────────────────┐  │     │ → chunking                  │       ┌──────────────────┐
│ Watched folder    │──┘     └──────────────┬──────────────┘       │ Qdrant           │      ┌───────────────┐
│ data/files/       │                       ▼                      │ vectors+payload  │◀────▶│ POST /query   │
└───────────────────┘        ┌─────────────────────────────┐       │ (doc_id,version) │      │ OpenAI embed  │
┌───────────────────┐ triggers│ index_documents()           │──────▶└──────────────────┘      │ → top-k       │
│ SQL Server        │───────▶│  • content hash → skip same │       ┌──────────────────┐      │ → OpenAI chat │
│ tables            │ outbox │  • OpenAI embeddings (batch)│──────▶│ SQLite manifest  │      │ → cited answer│
└───────────────────┘ + poll │  • upsert new, delete stale │       │ doc_id → version │      └───────────────┘
                             └─────────────────────────────┘       └──────────────────┘
```

| Event | Detection | Action |
|---|---|---|
| New/changed file | upload + watchdog, SHA-256 | re-embed, replace old chunks |
| Deleted file | watchdog / startup scan | remove vectors |
| New/updated SQL row | outbox trigger + polling (row hash) | re-embed that row |
| Deleted SQL row | outbox DELETE + polling PK diff | remove vectors |
| App was offline | startup sync + first poll | catches up |

## Setup

### 1. Dependencies

```bash
cd AgenticRagBotERP   # or your clone path
python -m venv .venv
# Windows:  .\.venv\Scripts\activate
# Linux/mac: source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Qdrant

Local:

```bash
docker compose up -d
```

Or set `QDRANT_URL` and `QDRANT_API_KEY` in `.env` for Qdrant Cloud.

### 3. Environment

```bash
cp .env.example .env   # Windows: copy .env.example .env
```

Fill in at minimum:

| Variable | Purpose |
|---|---|
| `OPENAI_API_KEY` | Embeddings + chat |
| `QDRANT_URL` | Vector database |
| `DATABASE_URL` | SQL Server (optional; omit to run files-only) |

**SQL Server URL notes**

- Prefer `mssql+pyodbc` with [ODBC Driver 18 for SQL Server](https://learn.microsoft.com/sql/connect/odbc/download-odbc-driver-for-sql-server).
- URL-encode password special characters (`@` → `%40`, etc.).
- Alternative without ODBC: `mssql+pymssql://USER:PASSWORD@HOST:1433/DBNAME`.

### 4. SQL sources

Edit `sql_sources.yaml`: one entry per table or custom `query`, with `primary_key` and `text_columns` (only human-readable fields — never passwords or huge blobs).

Example (custom query with join):

```yaml
sources:
  - name: pm_rag_tools
    query: >
      SELECT t.Id, t.Description, t.ProjectName, t.Level, l.Name AS LevelName
      FROM dbo.PMRagTool t
      LEFT JOIN dbo.PMRagToolLevel l ON t.Level = l.Id
    primary_key: Id
    text_columns: [Description, ProjectName, LevelName]
    metadata_columns: [Id, Level]
    interval_seconds: 60
```

After changing YAML, restart the API or call `POST /sync/sql`.

### 5. Optional: real-time SQL (outbox)

1. Run `sql/outbox_sqlserver.sql` in SSMS (outbox table + one trigger per indexed table).
2. Set `REALTIME_OUTBOX=true` in `.env`.
3. Grant the app login `SELECT` on indexed tables and `SELECT, DELETE` on `dbo.rag_outbox`.

Until the outbox exists, leave `REALTIME_OUTBOX=false` and rely on polling (`interval_seconds`).

### 6. Run

```bash
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

Open http://localhost:8000

**Test DB connection** (when `DATABASE_URL` is set):

```bash
python -c "from sqlalchemy import create_engine,text;from app.config import settings;print(create_engine(settings.database_url).connect().execute(text('select 1')).scalar())"
```

## Web UI

| Section | What it does |
|---|---|
| **SQL database (live)** | Reads `dbo.PMRagTool` directly from SQL Server (not the vector index) |
| **Ingest SQL → knowledge base** | Embeds all `sql_sources.yaml` entries into Qdrant |
| **Ask** | Default searches **files + SQL**; dropdown limits to `file` or `sql` only |
| **Indexed** | Manifest stats (`file` vs `sql` document counts) |

## API

| Method | Path | Description |
|---|---|---|
| `GET` | `/` | Web UI |
| `POST` | `/upload` | Upload and index files |
| `POST` | `/query` | RAG Q&A JSON: `question`, `top_k`, optional `source_type` (`file` \| `sql`) |
| `POST` | `/sync/sql` | Force SQL ingest into Qdrant |
| `GET` | `/stats` | Indexed document counts |
| `GET` | `/documents` | List manifest entries |
| `GET` | `/health` | Health + configured SQL source names |
| `GET` | `/sql/pm-rag-tools` | Live `PMRagTool` rows; optional `?project_name=PeopleManager` |
| `GET` | `/sql/preview/{source_name}` | Live preview for a `sql_sources.yaml` name |

### Examples

```bash
# Upload
curl -F "files=@report.pdf" localhost:8000/upload

# Ask (files + SQL)
curl -X POST localhost:8000/query -H "Content-Type: application/json" \
  -d "{\"question\":\"What tools exist for PeopleManager?\",\"top_k\":6}"

# SQL only
curl -X POST localhost:8000/query -H "Content-Type: application/json" \
  -d "{\"question\":\"What does the HR Policy module do?\",\"source_type\":\"sql\"}"

# Ingest SQL now
curl -X POST localhost:8000/sync/sql

curl localhost:8000/stats
curl "localhost:8000/sql/pm-rag-tools?project_name=PeopleManager"
```

**Document IDs**

- Files: `file:data/files/yourfile.pdf`
- SQL: `sql:<source_name>:<primary_key>` (e.g. `sql:pm_rag_tools:3`)

## Operations notes

- **Embedding model change**: delete the Qdrant collection and `data/manifest.db`, then re-ingest.
- **Cost**: unchanged rows/files are skipped via content hashing; only deltas call the embeddings API.
- **Custom `query:` sources**: row-level outbox updates are not supported; changes trigger a full re-sync of that source.
- **Security**: do not commit `.env`; use read-only DB credentials where possible; add API auth before public deployment.
- Scanned PDFs need OCR; convert legacy `.doc` to `.docx`.

## License / upstream

Based on the [rag-system](https://github.com/Shahid-Sheimi/rag-system) template; extended with SQL live preview, PMRagTool UI, and Alci-oriented `sql_sources.yaml` examples.
