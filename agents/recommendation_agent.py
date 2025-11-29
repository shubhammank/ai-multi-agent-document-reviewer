from .agent_base import AgentBase

class RecommendationAgent(AgentBase):
    def __init__(self):
        super().__init__(
            role="recommendation",
            system_prompt="Generate improvement suggestions and strategic recommendations."
        )
