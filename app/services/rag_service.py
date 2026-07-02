import json
from pathlib import Path

import faiss
import numpy as np

from app.services.embedding_service import embed_text

VECTOR_DIR = Path("vector_store")

index = faiss.read_index(str(VECTOR_DIR / "arzopa.index"))

with open(VECTOR_DIR / "documents.json", "r", encoding="utf-8") as f:
    documents = json.load(f)

def search_context(query: str, top_k: int = 4) -> str:
    query_vector = np.array([embed_text(query)]).astype("float32")
    faiss.normalize_L2(query_vector)

    scores, indices = index.search(query_vector, top_k)

    results = []

    for score, doc_index in zip(scores[0], indices[0]):
        if doc_index == -1:
            continue

        doc = documents[doc_index]
        results.append(
            f"Nguồn: {doc['source']}\nNội dung:\n{doc['content']}"
        )

    return "\n\n---\n\n".join(results)