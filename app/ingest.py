"""Single entry point for writing to the knowledge base. Files and SQL rows both go through
index_documents(), so they share the same versioning / dedupe / cleanup behavior."""
import hashlib, logging, threading
from dataclasses import dataclass, field
from pathlib import Path

from . import vectorstore
from .chunking import chunk_sections
from .config import FILES_DIR
from .embeddings import embed_documents
from .loaders import load_file
from .manifest import manifest

log = logging.getLogger("ingest")
_lock = threading.RLock()  # one writer at a time (upload API, watcher, SQL sync all write)


@dataclass
class Doc:
    doc_id: str
    source_type: str                 # "file" | "sql"
    version: str                     # content hash
    chunks: list = field(default_factory=list)   # [(text, meta)]
    title: str = ""


def index_documents(docs: list[Doc]):
    with _lock:
        texts, owners = [], []
        for d in docs:
            for i, (t, m) in enumerate(d.chunks):
                texts.append(t)
                owners.append((d, i, m))
        points = []
        if texts:
            vectors = embed_documents(texts)
            for (d, i, m), t, v in zip(owners, texts, vectors):
                points.append({
                    "id": vectorstore.point_id(d.doc_id, i),
                    "vector": v,
                    "payload": {"text": t, "doc_id": d.doc_id, "source_type": d.source_type,
                                "version": d.version, "chunk_index": i, "title": d.title, "meta": m},
                })
            vectorstore.upsert_points(points)
        for d in docs:
            vectorstore.delete_stale(d.doc_id, d.version)   # drop old-version chunks
            manifest.upsert(d.doc_id, d.source_type, d.version, len(d.chunks), d.title)


def remove_doc(doc_id: str):
    with _lock:
        vectorstore.delete_doc(doc_id)
        manifest.delete(doc_id)
        log.info("removed %s", doc_id)


# ---------- files ----------
def file_doc_id(path: Path) -> str:
    rel = path.resolve().relative_to(FILES_DIR.resolve())
    return "file:" + rel.as_posix()


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def ingest_file(path: Path, force: bool = False) -> dict:
    path = Path(path)
    doc_id = file_doc_id(path)
    with _lock:
        version = _sha256(path)
        if not force and manifest.get_version(doc_id) == version:
            return {"doc_id": doc_id, "status": "unchanged"}
        sections = load_file(path)
        chunks = chunk_sections([(t, {**m, "file": path.name}) for t, m in sections])
        index_documents([Doc(doc_id, "file", version, chunks, title=path.name)])
        log.info("indexed %s (%d chunks)", doc_id, len(chunks))
        return {"doc_id": doc_id, "status": "indexed", "chunks": len(chunks)}
