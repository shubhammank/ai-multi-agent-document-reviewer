import pytest
from chunking.semantic_chunker import SemanticChunker
from chunking.metadata_extractor import MetadataExtractor

@pytest.fixture
def sample_raw():
    return [
        {"text": "BASELINE EMISSIONS for 2023 were reported.", "type": "paragraph", "source": "pdf", "metadata": {}},
        {"text": "TARGET is to reduce emissions by 30%.", "type": "paragraph", "source": "pdf", "metadata": {}},
        {"text": "Scope 1 | 200 | 180 | 150", "type": "table_row", "source": "pdf", "metadata": {}},
    ]

def test_chunker_runs(sample_raw):
    chunker = SemanticChunker()
    enriched = MetadataExtractor.enrich(sample_raw, "dummy.pdf")
    chunks = chunker.process(enriched)
    assert len(chunks) > 0

def test_chunker_produces_text(sample_raw):
    chunker = SemanticChunker()
    enriched = MetadataExtractor.enrich(sample_raw, "dummy.pdf")
    chunks = chunker.process(enriched)
    for c in chunks:
        assert "text" in c
        assert len(c["text"]) > 0
