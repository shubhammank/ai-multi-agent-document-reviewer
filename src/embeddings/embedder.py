import yaml
from sentence_transformers import SentenceTransformer
from openai import OpenAI
import anthropic

class Embedder:
    """
    Supports multiple embedding backends:
    - sentence-transformers (default)
    - OpenAI text-embedding-3-small / large
    - Anthropic Claude Embeddings
    """

    def __init__(self, config_path="config/llm.yaml"):
        with open(config_path, "r") as f:
            cfg = yaml.safe_load(f)

        self.backend = cfg["embedding_backend"]
        self.model_name = cfg["embedding_model"]

        if self.backend == "sentence-transformers":
            self.model = SentenceTransformer(self.model_name, device="cpu")

        elif self.backend == "openai":
            self.client = OpenAI(api_key=cfg["openai_api_key"])

        elif self.backend == "anthropic":
            self.client = anthropic.Client(api_key=cfg["anthropic_api_key"])

    def embed(self, text: str):
        text = text.replace("\n", " ")
        if self.backend == "sentence-transformers":
            return self.model.encode(text, normalize_embeddings=True).tolist()

        elif self.backend == "openai":
            response = self.client.embeddings.create(
                model=self.model_name,
                input=text
            )
            return response.data[0].embedding

        elif self.backend == "anthropic":
            raise NotImplementedError("Anthropic embeddings coming soon")
