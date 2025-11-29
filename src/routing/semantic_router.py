from src.embeddings.embedder import Embedder

class SemanticRouter:
    """
    Uses semantic similarity to map text chunks to routing buckets.
    """

    CATEGORY_PROMPTS = {
        "recommendation": "This text requires improvement, suggestions, or next steps.",
        "evidence": "This text contains numerical data, KPIs, metrics, or measurable results.",
        "clarification": "This text contains ambiguity or statements needing more detail.",
        "proofreading": "This text may contain grammar, spelling, formatting or stylistic issues."
    }

    def __init__(self):
        self.embedder = Embedder()
        self.category_vectors = {
            cat: self.embedder.embed(desc)
            for cat, desc in self.CATEGORY_PROMPTS.items()
        }

    def best_category(self, text):
        vector = self.embedder.embed(text)

        best = None
        best_sim = -999

        for cat, vec in self.category_vectors.items():
            sim = self._cosine_sim(vec, vector)
            if sim > best_sim:
                best = cat
                best_sim = sim

        return best

    def _cosine_sim(self, a, b):
        import numpy as np
        a, b = np.array(a), np.array(b)
        return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))
