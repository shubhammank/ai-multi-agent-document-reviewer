class ContextBuilder:
    """
    Adds left/right context to chunks to prevent semantic drift.
    """

    @staticmethod
    def build(chunks, overlap=30):
        enriched = []

        for idx, c in enumerate(chunks):
            left = chunks[idx - 1]["text"][-overlap:] if idx > 0 else None
            right = chunks[idx + 1]["text"][:overlap] if idx < len(chunks) - 1 else None

            enriched.append({
                "text": c["text"],
                "source_items": c["source_items"],
                "left_context": left,
                "right_context": right
            })

        return enriched
