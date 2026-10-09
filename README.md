# RAG Knowledge Base: PDF / CSV / Word uploads + live SQL Server sync (OpenAI)

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

### How SQL Server changes reach the RAG in near real time
1. A T-SQL trigger on each table writes `(table, pk, op)` into `dbo.rag_outbox` on every INSERT/UPDATE/DELETE.
2. The app's outbox worker drains that table every ~2 seconds, de-duplicates, loads **only the changed rows**, and re-embeds them (about 2-4 s end to end).
3. Deleted rows have their vectors removed.
4. A slower polling job (`interval_seconds`) reconciles the whole table (hash compare + PK diff), so missed events or app downtime are self-healing.

| Event | Detection | Action |
|---|---|---|
| New/changed file (upload or edited on disk) | upload endpoint + watchdog, SHA-256 | re-embed, replace old chunks |
| Deleted file | watchdog / startup scan | remove vectors |
| New/updated SQL row | outbox trigger + polling (row hash) | re-embed that row |
| Deleted SQL row | outbox DELETE + polling PK diff | remove vectors |
| App was offline | startup scan + first poll | catches up |

## Setup

```bash
unzip rag-system.zip && cd rag-system
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
docker compose up -d                      # Qdrant
```

1. **Edit `.env`**: `OPENAI_API_KEY`, `DATABASE_URL`, and `LLM_MODEL` if your account uses a different chat model.
   * pyodbc needs the **Microsoft ODBC Driver 18 for SQL Server** installed (https://learn.microsoft.com/sql/connect/odbc/download-odbc-driver-for-sql-server).
     No driver install? Use `mssql+pymssql://USER:PASSWORD@HOST:1433/DBNAME` instead.
   * URL-encode special characters in the password (`@` → `%40`, `:` → `%3A`, `/` → `%2F`, `#` → `%23`).
2. **Edit `sql_sources.yaml`** with your tables (`schema.table`), primary key, and the text columns to embed.
3. **Enable real-time**: run `sql/outbox_sqlserver.sql` in SSMS (one trigger block per table). `REALTIME_OUTBOX=true` is already set in `.env`.
4. **Run**: `uvicorn app.main:app --port 8000` and open http://localhost:8000.

Test the DB connection:
```bash
python -c "from sqlalchemy import create_engine,text;from app.config import settings;print(create_engine(settings.database_url).connect().execute(text('select 1')).scalar())"
```

## API
```bash
curl -F "files=@report.pdf" -F "files=@sales.csv" -F "files=@policy.docx" localhost:8000/upload
curl -X POST localhost:8000/query -H 'Content-Type: application/json' -d '{"question":"...","top_k":6}'
curl -X POST localhost:8000/sync/sql        # force a SQL sync now
curl localhost:8000/stats ; curl localhost:8000/health
```

## Notes
* **DB permissions**: `SELECT` on the indexed tables, plus `SELECT, DELETE` on `dbo.rag_outbox`. Triggers must be created by an admin once.
* **Changing the embedding model**: vector size changes, so delete the Qdrant collection and `data/manifest.db`, then restart to re-index.
* **Cost**: unchanged data is never re-embedded (hash check). Only new or changed chunks call the embeddings API.
* **Don't embed** binary, ID-only or huge columns. List only meaningful text in `text_columns`.
* **Custom `query:` sources** work, but any change re-syncs the whole source (use `table:` for the cheap row-level path).
* **Scaling out**: single worker by default; for several workers/servers move the manifest to SQL Server and run ingestion as one separate worker.
* **Security**: add authentication to the API before exposing it, use a read-only DB login, keep `.env` out of git.
* Scanned PDFs need OCR; convert legacy `.doc` to `.docx`.
