"""Watches data/files so files dropped / edited / deleted on disk are synced automatically."""
import logging, time
from pathlib import Path
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from .config import FILES_DIR, SUPPORTED_EXT
from .ingest import file_doc_id, ingest_file, remove_doc
from .manifest import manifest

log = logging.getLogger("watcher")


def _ok(p: Path) -> bool:
    return p.suffix.lower() in SUPPORTED_EXT and not p.name.startswith(("~$", "."))


class Handler(FileSystemEventHandler):
    def _index(self, p: Path):
        if not _ok(p):
            return
        for attempt in range(4):           # file may still be mid-write
            try:
                time.sleep(1.0)
                ingest_file(p)
                return
            except Exception as e:
                log.warning("ingest retry %s (%s)", p.name, e)
        log.error("giving up on %s", p)

    def on_created(self, e):
        if not e.is_directory: self._index(Path(e.src_path))

    def on_modified(self, e):
        if not e.is_directory: self._index(Path(e.src_path))

    def on_deleted(self, e):
        p = Path(e.src_path)
        if not e.is_directory and _ok(p):
            remove_doc(file_doc_id(p))

    def on_moved(self, e):
        if e.is_directory: return
        if _ok(Path(e.src_path)): remove_doc(file_doc_id(Path(e.src_path)))
        self._index(Path(e.dest_path))


def initial_scan():
    """On startup: index anything new/changed and drop anything deleted while we were offline."""
    on_disk = set()
    for p in FILES_DIR.rglob("*"):
        if p.is_file() and _ok(p):
            on_disk.add(file_doc_id(p))
            try:
                ingest_file(p)
            except Exception:
                log.exception("failed to ingest %s", p)
    for doc_id in manifest.ids_with_prefix("file:") - on_disk:
        remove_doc(doc_id)


def start() -> Observer:
    obs = Observer()
    obs.schedule(Handler(), str(FILES_DIR), recursive=True)
    obs.start()
    return obs
