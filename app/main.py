import logging, shutil, threading
from contextlib import asynccontextmanager
from datetime import datetime
from pathlib import Path

from apscheduler.schedulers.background import BackgroundScheduler
from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.responses import FileResponse
from pydantic import BaseModel

from . import vectorstore, watcher
from .config import FILES_DIR, SUPPORTED_EXT, settings
from .ingest import ingest_file, remove_doc
from .manifest import manifest
from .rag import answer
from .sql_sync import listen_forever, load_sources, outbox_worker, sync_source

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
SOURCES = load_sources()


@asynccontextmanager
async def lifespan(app: FastAPI):
    vectorstore.ensure_collection()
    threading.Thread(target=watcher.initial_scan, daemon=True).start()
    observer = watcher.start()

    sched = BackgroundScheduler()
    for s in SOURCES:   # polling = safety net that also catches deletes / missed notifications
        sched.add_job(sync_source, "interval", seconds=s.interval_seconds, args=[s],
                      id=f"sql-{s.name}", max_instances=1, coalesce=True, next_run_time=datetime.now())
    sched.start()
    if SOURCES and settings.realtime_postgres:
        threading.Thread(target=listen_forever, args=(SOURCES,), daemon=True).start()
    if SOURCES and settings.realtime_outbox:
        threading.Thread(target=outbox_worker, args=(SOURCES,), daemon=True).start()
    yield
    observer.stop()
    sched.shutdown(wait=False)


app = FastAPI(title="RAG Knowledge Base", lifespan=lifespan)


class Query(BaseModel):
    question: str
    top_k: int = 6
    source_type: str | None = None   # "file" | "sql" | None (all)


@app.get("/")
def home():
    return FileResponse("static/index.html")


@app.post("/upload")
def upload(files: list[UploadFile] = File(...)):
    results = []
    for f in files:
        name = Path(f.filename).name
        if Path(name).suffix.lower() not in SUPPORTED_EXT:
            results.append({"file": name, "status": "rejected", "reason": f"allowed: {sorted(SUPPORTED_EXT)}"})
            continue
        dest = FILES_DIR / name
        with open(dest, "wb") as out:
            shutil.copyfileobj(f.file, out)
        try:
            results.append({"file": name, **ingest_file(dest)})
        except Exception as e:
            results.append({"file": name, "status": "error", "reason": str(e)})
    return results


@app.post("/query")
def query(q: Query):
    return answer(q.question, q.top_k, q.source_type)


@app.get("/documents")
def documents(source_type: str | None = None, limit: int = 500):
    return manifest.list(source_type, limit)


@app.get("/stats")
def stats():
    return manifest.stats()


@app.delete("/documents")
def delete_document(doc_id: str):
    if doc_id.startswith("file:"):
        p = FILES_DIR / doc_id[5:]
        if p.exists():
            p.unlink()
    elif doc_id.startswith("sql:"):
        raise HTTPException(400, "SQL rows are managed by the database; delete the row there.")
    remove_doc(doc_id)
    return {"deleted": doc_id}


@app.post("/sync/sql")
def sync_sql_now():
    """Manual 'sync now' button."""
    return [sync_source(s) for s in SOURCES]


@app.get("/health")
def health():
    return {"ok": True, "sql_sources": [s.name for s in SOURCES],
            "realtime_outbox": settings.realtime_outbox, "realtime_postgres": settings.realtime_postgres}
