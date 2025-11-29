import pytest
from unittest.mock import patch
from orchestrator.review_orchestrator import ReviewOrchestrator

@pytest.fixture
def orchestrator():
    return ReviewOrchestrator()

@patch("ingestion.pdf_reader.PDFReader.load", return_value=[
    {"text": "Baseline emissions are 150.", "type": "paragraph", "source": "pdf", "metadata": {}}
])
@patch("ingestion.ocr_engine.OCREngine.load", return_value=[])
@patch("chunking.semantic_chunker.SemanticChunker.process", return_value=[
    {"id": "chunk-0", "text": "Baseline emissions are 150.", "metadata": {}, "density": 0.2}
])
@patch("embeddings.embedder.Embedder.embed", return_value=[0.1, 0.2])
@patch("embeddings.vector_store.VectorStore.query", return_value={"ids": [["chunk-0"]]})
@patch("agents.agent_base.AgentBase.call_llm", return_value={
    "comment": "Mocked pipeline test comment",
    "severity": "medium",
    "justification": "Mocked justification"
})
def test_full_pipeline(mock_a, mock_b, mock_c, mock_d, mock_e, mock_f, orchestrator):
    result = orchestrator.run("dummy.pdf")
    assert len(result) == 1
    assert result[0]["response"]["comment"] == "Mocked pipeline test comment"
