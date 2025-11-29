from langgraph.graph import StateGraph, END

class ReviewState(dict):
    pass

class GraphBuilder:
    """
    LangGraph orchestration:
    ingestion → chunking → embeddings → routing → agents → merge
    """

    def __init__(self, orchestrator):
        self.orchestrator = orchestrator

    def build(self):
        graph = StateGraph(ReviewState)

        graph.add_node("ingest", self.orchestrator.step_ingest)
        graph.add_node("chunk", self.orchestrator.step_chunk)
        graph.add_node("embed", self.orchestrator.step_embed)
        graph.add_node("route", self.orchestrator.step_route)
        graph.add_node("agents", self.orchestrator.step_agents)
        graph.add_node("merge", self.orchestrator.step_merge)

        graph.set_entry_point("ingest")

        graph.add_edge("ingest", "chunk")
        graph.add_edge("chunk", "embed")
        graph.add_edge("embed", "route")
        graph.add_edge("route", "agents")
        graph.add_edge("agents", "merge")
        graph.add_edge("merge", END)

        return graph.compile()
