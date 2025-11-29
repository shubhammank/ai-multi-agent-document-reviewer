from .agent_base import AgentBase

class ClarificationAgent(AgentBase):
    def __init__(self):
        super().__init__(
            role="clarification",
            system_prompt="Identify unclear statements and generate clarification questions."
        )
