from functools import lru_cache
from .config import settings


@lru_cache
def _openai():
    from openai import OpenAI
    return OpenAI(api_key=settings.openai_api_key, max_retries=5, timeout=60)


@lru_cache
def _local():
    from sentence_transformers import SentenceTransformer
    return SentenceTransformer(settings.embedding_model)


def _openai_embed(texts: list[str], batch: int = 100) -> list[list[float]]:
    out: list[list[float]] = []
    for i in range(0, len(texts), batch):
        chunk = [t.replace("\x00", " ") or " " for t in texts[i:i + batch]]
        resp = _openai().embeddings.create(model=settings.embedding_model, input=chunk)
        out.extend(d.embedding for d in sorted(resp.data, key=lambda d: d.index))
    return out


def embed_documents(texts: list[str]) -> list[list[float]]:
    if settings.embedding_provider == "openai":
        return _openai_embed(texts)
    return _local().encode(texts, batch_size=32, normalize_embeddings=True,
                           show_progress_bar=False).tolist()


def embed_query(query: str) -> list[float]:
    if settings.embedding_provider == "openai":
        return _openai_embed([query])[0]
    return _local().encode(settings.query_prefix + query, normalize_embeddings=True).tolist()
