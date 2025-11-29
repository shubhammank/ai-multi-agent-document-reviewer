from .agent_base import AgentBase

class ProofreadingAgent(AgentBase):
    def __init__(self):
        super().__init__(
            role="proofreading",
            system_prompt="Detect grammar, spelling, formatting, or structure issues."
        )
