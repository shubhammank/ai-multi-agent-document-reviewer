class MetadataExtractor:
    """
    Adds IDs, ordering, and normalized metadata to ingestion chunks.
    """

    @staticmethod
    def enrich(chunks: list, file_path: str):
        enriched = []

        for idx, c in enumerate(chunks):
            enriched.append({
                "id": f"{file_path}-chunk-{idx}",
                "text": c["text"],
                "type": c.get("type", "text"),
                "source": c["source"],
                "metadata": c.get("metadata", {}) | {
                    "chunk_index": idx
                }
            })

        return enriched
