import uuid
from qdrant_client import QdrantClient, models
from .config import settings

client = QdrantClient(url=settings.qdrant_url, api_key=settings.qdrant_api_key or None)
C = settings.collection


def ensure_collection():
    if not client.collection_exists(C):
        client.create_collection(
            C,
            vectors_config=models.VectorParams(size=settings.embedding_dim, distance=models.Distance.COSINE),
        )
    for field in ("doc_id", "source_type", "version"):
        try:
            client.create_payload_index(C, field, models.PayloadSchemaType.KEYWORD)
        except Exception:
            pass  # already exists


def point_id(doc_id: str, chunk_index: int) -> str:
    # Deterministic: re-indexing the same doc overwrites instead of duplicating.
    return str(uuid.uuid5(uuid.NAMESPACE_URL, f"{doc_id}#{chunk_index}"))


def upsert_points(points: list[dict], batch: int = 128):
    for i in range(0, len(points), batch):
        client.upsert(
            C,
            points=[models.PointStruct(id=p["id"], vector=p["vector"], payload=p["payload"])
                    for p in points[i:i + batch]],
            wait=True,
        )


def delete_stale(doc_id: str, current_version: str):
    """Remove chunks of this doc that belong to an older version (done AFTER the new
    version is written, so queries never see a gap)."""
    client.delete(
        C,
        points_selector=models.FilterSelector(filter=models.Filter(
            must=[models.FieldCondition(key="doc_id", match=models.MatchValue(value=doc_id))],
            must_not=[models.FieldCondition(key="version", match=models.MatchValue(value=current_version))],
        )),
        wait=True,
    )


def delete_doc(doc_id: str):
    client.delete(
        C,
        points_selector=models.FilterSelector(filter=models.Filter(
            must=[models.FieldCondition(key="doc_id", match=models.MatchValue(value=doc_id))]
        )),
        wait=True,
    )


def search(vector: list[float], k: int, source_type: str | None = None):
    flt = None
    if source_type:
        flt = models.Filter(must=[models.FieldCondition(key="source_type", match=models.MatchValue(value=source_type))])
    return client.query_points(C, query=vector, limit=k, query_filter=flt, with_payload=True).points
