from functools import lru_cache
from . import vectorstore
from .config import settings
from .embeddings import embed_query

SYSTEM = (
    "You answer questions using ONLY the provided context excerpts. "
    "Cite the excerpts you used like [1], [2]. If the context does not contain the answer, "
    "say you could not find it in the knowledge base. Do not invent facts."
)


@lru_cache
def _client():
    from openai import OpenAI
    return OpenAI(api_key=settings.openai_api_key, max_retries=3, timeout=120)


def retrieve(question: str, top_k: int = 6, source_type: str | None = None, min_score: float = 0.0):
    hits = vectorstore.search(embed_query(question), top_k, source_type)
    return [
        {"text": h.payload["text"], "score": h.score, "doc_id": h.payload["doc_id"],
         "source_type": h.payload["source_type"], "title": h.payload.get("title", ""),
         "meta": h.payload.get("meta", {})}
        for h in hits if h.score >= min_score
    ]


def answer(question: str, top_k: int = 6, source_type: str | None = None) -> dict:
    hits = retrieve(question, top_k, source_type)
    if not hits:
        return {"answer": "I could not find anything relevant in the knowledge base.", "sources": []}
    context = "\n\n".join(
        f"[{i}] source={h['doc_id']} {h['meta']}\n{h['text']}" for i, h in enumerate(hits, 1)
    )
    resp = _client().chat.completions.create(
        model=settings.llm_model,
        max_completion_tokens=2048,
        messages=[
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": f"<context>\n{context}\n</context>\n\nQuestion: {question}"},
        ],
    )
    return {"answer": resp.choices[0].message.content or "", "sources": hits}
