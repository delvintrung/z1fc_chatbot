import json
from pathlib import Path

import faiss
import numpy as np

from app.services.embedding_service import embed_text

DATA_DIR = Path("app/data")
VECTOR_DIR = Path("vector_store")
VECTOR_DIR.mkdir(exist_ok=True)

def chunk_text(text: str, chunk_size: int = 800, overlap: int = 120):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start += chunk_size - overlap

    return chunks

def main():
    documents = []

    for file_path in DATA_DIR.glob("*.md"):
        text = file_path.read_text(encoding="utf-8")
        chunks = chunk_text(text)

        for index, chunk in enumerate(chunks):
            documents.append({
                "source": file_path.name,
                "chunk_index": index,
                "content": chunk,
            })

    embeddings = []

    for doc in documents:
        vector = embed_text(doc["content"])
        embeddings.append(vector)

    embedding_matrix = np.array(embeddings).astype("float32")

    faiss.normalize_L2(embedding_matrix)

    dimension = embedding_matrix.shape[1]
    index = faiss.IndexFlatIP(dimension)
    index.add(embedding_matrix)

    faiss.write_index(index, str(VECTOR_DIR / "arzopa.index"))

    with open(VECTOR_DIR / "documents.json", "w", encoding="utf-8") as f:
        json.dump(documents, f, ensure_ascii=False, indent=2)

    print(f"Indexed {len(documents)} chunks.")

if __name__ == "__main__":
    main()