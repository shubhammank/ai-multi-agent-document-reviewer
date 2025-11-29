import yaml
from sentence_transformers import SentenceTransformer
from .density_analyzer import DensityAnalyzer
from .boundary_detector import BoundaryDetector
from .context_builder import ContextBuilder
from src.utils.text_cleaner import TextCleaner

class SemanticChunker:
    """
    Hybrid chunker combining:
    - Layout-aware raw segments
    - Semantic grouping using embeddings
    - Recursive text splitting (if needed)
    """

    def __init__(self, config_path="config/chunking.yaml"):
        with open(config_path, "r") as f:
            self.config = yaml.safe_load(f)

        self.max_chunk = self.config["chunk_size"]
        self.min_chunk = self.config["min_chunk"]
        self.overlap = self.config["overlap"]
        self.embedding_model = SentenceTransformer(self.config["embedding_model"])

    def embed(self, text):
        return self.embedding_model.encode(text, normalize_embeddings=True)

    def _recursive_split(self, text):
        """
        Fallback method when a raw element is too long.
        Uses simple recursive splitting on sentence boundaries.
        """

        if len(text.split()) <= self.max_chunk:
            return [text]

        # Split by sentences
        sentences = text.split(". ")
        chunks = []
        current = []

        for sent in sentences:
            current.append(sent)
            if len(" ".join(current).split()) >= self.max_chunk:
                chunks.append(" ".join(current))
                current = []

        if current:
            chunks.append(" ".join(current))

        return chunks

    def process(self, raw_items):
        """
        Steps:
        1. Clean text
        2. Density analysis
        3. Boundary detection
        4. Hybrid semantic chunking
        5. Context window build
        """

        cleaned = [
            {**i, "text": TextCleaner.clean(i["text"])} for i in raw_items
            if i["text"].strip()
        ]

        # 1. Density scoring
        DensityAnalyzer.add_density_scores(cleaned)

        # 2. Boundary detection
        boundaries = BoundaryDetector.find_boundaries(cleaned)

        # 3. Hybrid chunking
        chunks = []

        for boundary in boundaries:
            segment_items = cleaned[boundary[0]:boundary[1]]

            combined_text = " ".join([x["text"] for x in segment_items])

            # If segment fits into a chunk → store directly
            if len(combined_text.split()) <= self.max_chunk:
                chunks.append({
                    "text": combined_text,
                    "source_items": segment_items
                })
                continue

            # Otherwise recursive split
            recursive_parts = self._recursive_split(combined_text)
            for r in recursive_parts:
                chunks.append({
                    "text": r,
                    "source_items": segment_items
                })

        # 4. Add contextual windows
        final_chunks = ContextBuilder.build(chunks, overlap=self.overlap)

        # 5. Add indexes and structure
        normalized = []
        for idx, c in enumerate(final_chunks):
            normalized.append({
                "id": f"chunk-{idx}",
                "text": c["text"],
                "metadata": {
                    "left_context": c.get("left_context"),
                    "right_context": c.get("right_context"),
                    "source_items": c["source_items"]
                }
            })

        return normalized
