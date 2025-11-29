class DensityRouter:
    """
    Uses semantic density to guess routing:
    - High density → evidence
    - Low density → proofreading / clarification
    """

    def route(self, chunk):
        d = chunk.get("density", 0)

        if d > 0.15:
            return "evidence"
        if d < 0.03:
            return "proofreading"
        return "clarification"
