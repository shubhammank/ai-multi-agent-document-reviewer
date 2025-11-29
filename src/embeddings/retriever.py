from .vector_store import VectorStore
from .embedder import Embedder

class Retriever:
    """
    Top-k retriever for agents.
    """

    def __init__(self):
        self.embedder = Embedder()
        self.store = VectorStore()

    def search(self, query: str, top_k=5):
        vec = self.embedder.embed(query)
        results = self.store.query(vec, top_k=top_k)
        return results
