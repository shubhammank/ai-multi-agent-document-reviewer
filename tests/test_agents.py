import pytest
from unittest.mock import patch
from agents.recommendation_agent import RecommendationAgent
from agents.evidence_agent import EvidenceAgent
from agents.clarification_agent import ClarificationAgent
from agents.proofreading_agent import ProofreadingAgent

@pytest.fixture
def fake_chunk():
    return {"text": "This statement should improve its clarity."}

@patch("agents.agent_base.AgentBase.call_llm", return_value={
    "comment": "Mocked response",
    "severity": "low",
    "justification": "Mocked justification"
})
def test_recommendation_agent(mock_llm, fake_chunk):
    agent = RecommendationAgent()
    out = agent.run(fake_chunk)
    assert out["comment"] == "Mocked response"

@patch("agents.agent_base.AgentBase.call_llm", return_value={
    "comment": "Mock evidence",
    "severity": "medium",
    "justification": "Mocked"
})
def test_evidence_agent(mock_llm, fake_chunk):
    agent = EvidenceAgent()
    out = agent.run(fake_chunk)
    assert "Mock evidence" in out["comment"]

@patch("agents.agent_base.AgentBase.call_llm", return_value={
    "comment": "Needs clarification",
    "severity": "medium",
    "justification": "Mocked"
})
def test_clarification_agent(mock_llm, fake_chunk):
    agent = ClarificationAgent()
    out = agent.run(fake_chunk)
    assert out["comment"] == "Needs clarification"

@patch("agents.agent_base.AgentBase.call_llm", return_value={
    "comment": "Typo found",
    "severity": "low",
    "justification": "Mocked"
})
def test_proofreading_agent(mock_llm, fake_chunk):
    agent = ProofreadingAgent()
    out = agent.run(fake_chunk)
    assert "Typo" in out["comment"]
