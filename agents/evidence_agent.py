from .agent_base import AgentBase

class EvidenceAgent(AgentBase):
    def __init__(self):
        super().__init__(
            role="evidence",
            system_prompt="Extract evidence-based insights, KPIs, metrics, or factual validations."
        )
