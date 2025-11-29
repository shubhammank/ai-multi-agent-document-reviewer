# Multi-Agent Document Reviewer (GenAI + RAG 2.0 + LangGraph)

This repository contains a complete production-grade Multi-Agent Document Review System built using Large Language Models, Semantic Chunking, Vector Embeddings, Delta Refresh Indexing, Rule-Based and Semantic Routing, and LangGraph-based Orchestration. The system processes PDF and DOCX files, intelligently chunks and routes them, and generates structured review comments using specialized LLM agents.

The solution is designed for enterprise-grade ESG report review, audit document processing, compliance review automation, and any workflow that requires intelligent multi-agent document analysis.

-------------------------------------------------------------------------------

## Key Features

### Multi-Agent LLM System
The system includes four specialized LLM agents:
- Recommendation Agent
- Evidence Agent
- Clarification Agent
- Proofreading Agent

Each agent uses structured JSON output and follows strict system prompts to ensure quality and consistency.

### Ingestion Layer
- PDF extraction using high-resolution layout parsing
- DOCX parsing (paragraphs and tables)
- OCR fallback for scanned PDFs
- Metadata enrichment

### Semantic Chunking Engine
Hybrid chunking approach combining:
- Semantic density analysis
- Boundary detection (headings, tables, density jumps)
- Recursive sentence-level splitting
- Context window generation
- Metadata normalization

### Embeddings and Vector Store
- Sentence Transformers embedding
- Optional OpenAI embedding support
- ChromaDB vector database
- Delta-Embedding Refresh for performance optimization

### Routing Engine
Three-layer hybrid routing:
1. Keyword rules (YAML)
2. Density-based routing
3. Semantic similarity routing
Final routing guarantees accurate agent assignment.

### LangGraph Orchestration Pipeline
End-to-end execution pipeline:
Ingest → Chunk → Embed → Route → Agents → Merge → Final Output

### FastAPI Microservice
- POST /review for file submission
- GET /health for monitoring
- CORS enabled
- OpenAPI specification included

-------------------------------------------------------------------------------

## Folder Structure

ai-multi-agent-document-reviewer/
README.md
requirements.txt
docker-compose.yml
Dockerfile
.env.example
main.py

src/
    ingestion/
    chunking/
    embeddings/
    routing/
    orchestrator/
    schemas/
    utils/

agents/
api/
config/
docs/
tests/
notebooks/
samples/

-------------------------------------------------------------------------------

## Installation

Clone the repository:

git clone https://github.com/yourusername/ai-multi-agent-document-reviewer.git
cd ai-multi-agent-document-reviewer

Install required packages:

pip install -r requirements.txt

Copy environment variables:

cp .env.example .env

Set your OpenAI or Anthropic API keys inside .env.

-------------------------------------------------------------------------------

## Running the API

Start FastAPI server:

uvicorn api.server:app --reload --port 8000

API documentation will be available at:

http://localhost:8000/docs

-------------------------------------------------------------------------------

## Running the Review Pipeline Programmatically

from orchestrator.review_orchestrator import ReviewOrchestrator

orchestrator = ReviewOrchestrator()
results = orchestrator.run("samples/sample_esg_report.pdf")
print(results)

-------------------------------------------------------------------------------

## Docker Deployment

Build and run using docker-compose:

docker-compose up --build

This starts the API at:

http://localhost:8000

-------------------------------------------------------------------------------

## Output Format

Each agent returns structured JSON:

[
  {
    "category": "evidence",
    "chunk_id": "chunk-12",
    "response": {
      "comment": "Add a baseline reference for comparison.",
      "severity": "medium",
      "justification": "This statement shows progress but does not refer to the baseline year."
    }
  }
]

-------------------------------------------------------------------------------

## Configuration

All system configurations are stored in the config folder:
- chunking.yaml
- llm.yaml
- metadata.yaml
- routing_rules.yaml

These files control chunking size, embedding models, LLM backend, routing rules, and metadata enrichment behavior.

-------------------------------------------------------------------------------

## Documentation

All architecture and process documentation is inside the docs folder:
- Full architecture breakdown
- Routing logic
- Sequence diagrams
- Agent design
- UML diagrams using PlantUML

-------------------------------------------------------------------------------

## Unit Tests

Run all tests using:

pytest tests

Tests include:
- Chunker tests
- Router tests
- Agent tests (mocked LLM calls)
- End-to-end pipeline test

-------------------------------------------------------------------------------

## Demo Notebook

A full demo notebook is included:

notebooks/demo.ipynb

This notebook demonstrates:
- Loading documents
- Running the review pipeline
- Inspecting chunks
- Performing similarity search
- Exporting results to JSON

-------------------------------------------------------------------------------

## Sample Documents

Sample ESG documents for testing are provided in the samples folder:
- PDF sample
- DOCX sample
- Table-heavy sample

-------------------------------------------------------------------------------

## Use Cases

This system can be used for:
- ESG Report Review Automation
- Financial & Compliance Document Review
- Legal Document Analysis
- Semantic Content Audits
- Large-Scale Text Analysis with Multi-Agent Systems
- RAG 2.0 Enterprise Document Intelligence

-------------------------------------------------------------------------------

## Technology Stack

- Python 3.10
- LangChain
- LangGraph
- ChromaDB
- Sentence Transformers
- FastAPI
- OpenAI or Anthropic LLMs
- Tesseract OCR
- pytest
- PlantUML
- Docker

-------------------------------------------------------------------------------

## License

MIT License

-------------------------------------------------------------------------------

## Author

Your Name
AI Architect and GenAI Developer

-------------------------------------------------------------------------------
