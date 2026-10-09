from langchain_text_splitters import RecursiveCharacterTextSplitter
from .config import settings

_splitter = RecursiveCharacterTextSplitter(
    chunk_size=settings.chunk_size,
    chunk_overlap=settings.chunk_overlap,
    separators=["\n\n", "\n", ". ", " ", ""],
)


def chunk_sections(sections):
    """sections: iterable of (text, meta) -> list of (chunk_text, meta)"""
    out = []
    for text, meta in sections:
        for piece in _splitter.split_text(text):
            if piece.strip():
                out.append((piece, dict(meta)))
    return out
