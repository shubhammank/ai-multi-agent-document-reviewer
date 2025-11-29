import chromadb
from chromadb.config import Settings
import os

class VectorStore:
    """
    Wrapper around ChromaDB with a clean API:
    - add_documents()
    - query()
    - reset()
    """

    def __init__(self, persist_dir="vector_store", collection_name="doc_chunks"):
        os.makedirs(persist_dir, exist_ok=True)

        self.client = chromadb.Client(
            Settings(chroma_db_impl="duckdb+parquet", persist_directory=persist_dir)
        )

        self.collection = self.client.get_or_create_collection(
            name=collection_name,
            metadata={"hnsw:space": "cosine"}
        )

    def reset(self):
        self.client.delete_collection("doc_chunks")
        self.collection = self.client.get_or_create_collection("doc_chunks")

    def add_documents(self, ids, embeddings, metadatas, documents):
        self.collection.add(
            ids=ids,
            embeddings=embeddings,
            metadatas=metadatas,
            documents=documents
        )

    def query(self, text_embedding, top_k=5):
        return self.collection.query(
            query_embeddings=[text_embedding],
            n_results=top_k
        )
