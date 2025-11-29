from ingestion.pdf_reader import PDFReader
from ingestion.docx_reader import DOCXReader
from ingestion.ocr_engine import OCREngine
from chunking.semantic_chunker import SemanticChunker
from chunking.metadata_extractor import MetadataExtractor
from embeddings.embedder import Embedder
from embeddings.vector_store import VectorStore
from embeddings.delta_manager import DeltaManager
from routing.router import Router
from agents.recommendation_agent import RecommendationAgent
from agents.evidence_agent import EvidenceAgent
from agents.clarification_agent import ClarificationAgent
from agents.proofreading_agent import ProofreadingAgent
from .graph_builder import GraphBuilder

class ReviewOrchestrator:

    def __init__(self):
        self.pdf = PDFReader()
        self.docx = DOCXReader()
        self.ocr = OCREngine()
        self.chunker = SemanticChunker()
        self.embedder = Embedder()
        self.vs = VectorStore()
        self.router = Router()
        self.agents = {
            "recommendation": RecommendationAgent(),
            "evidence": EvidenceAgent(),
            "clarification": ClarificationAgent(),
            "proofreading": ProofreadingAgent()
        }

    # -----------------------
    # LangGraph pipeline steps
    # -----------------------

    def step_ingest(self, state):
        file_path = state["file_path"]
        ext = file_path.lower()

        if ext.endswith(".pdf"):
            raw = self.pdf.load(file_path)
            raw += self.ocr.load(file_path)
        else:
            raw = self.docx.load(file_path)

        state["raw"] = raw
        return state

    def step_chunk(self, state):
        raw = state["raw"]
        meta = MetadataExtractor.enrich(raw, state["file_path"])
        chunks = self.chunker.process(meta)
        state["chunks"] = chunks
        return state

    def step_embed(self, state):
        if DeltaManager.needs_update(state["file_path"], state["chunks"]):
            self.vs.reset()

            ids, embeds, metas, docs = [], [], [], []
            for c in state["chunks"]:
                ids.append(c["id"])
                embeds.append(self.embedder.embed(c["text"]))
                metas.append(c["metadata"])
                docs.append(c["text"])

            self.vs.add_documents(ids, embeds, metas, docs)
            DeltaManager.update_state(state["file_path"], state["chunks"])

        return state

    def step_route(self, state):
        routed = []
        for c in state["chunks"]:
            category = self.router.route(c)
            routed.append({"chunk": c, "category": category})
        state["routed"] = routed
        return state

    def step_agents(self, state):
        outputs = []

        for item in state["routed"]:
            agent = self.agents[item["category"]]
            result = agent.run(item["chunk"])
            outputs.append({
                "category": item["category"],
                "chunk_id": item["chunk"]["id"],
                "response": result
            })

        state["agent_outputs"] = outputs
        return state

    def step_merge(self, state):
        # Simple merge
        state["final"] = state["agent_outputs"]
        return state

    # ---------------
    # Public API
    # ---------------

    def run(self, file_path):
        state = {"file_path": file_path}
        graph = GraphBuilder(self).build()
        result = graph.invoke(state)
        return result["final"]
