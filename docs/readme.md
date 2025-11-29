# Multi-Agent Document Reviewer (GenAI + RAG 2.0 + LangGraph)

A production-grade document review pipeline built using:

- Multi-Agent LLM System (Recommendation, Evidence, Clarification, Proofreading)
- Semantic Chunking (Hybrid layout + semantic + recursive)
- RAG 2.0 Retrieval with ChromaDB
- Delta Embedding Refresh (hash-based)
- LangGraph Orchestration Pipeline
- FastAPI Microservice + OpenAPI Integration

This platform automatically ingests PDF/DOCX documents, chunks them intelligently, embeds them, routes each chunk to the right LLM agent, and generates structured review comments.

---

## Features

### 1. Ingestion Layer
- PDF layout-aware extraction  
- DOCX parsing (paragraphs + tables)  
- OCR fallback using Tesseract  

### 2. Chunking Layer
- Semantic density scoring  
- Section boundary detection  
- Recursive sentence-level splitting  
- Context windows  
- Metadata enrichment  

### 3. Embedding Layer
- Sentence Transformers embedding  
- ChromaDB vector store  
- Delta update system  

### 4. Routing Layer
- Keyword rules (YAML)  
- Density-based routing  
- Semantic similarity routing  
- Hybrid final predictor  

### 5. Agent Layer (LLM-Powered)
- RecommendationAgent  
- EvidenceAgent  
- ClarificationAgent  
- ProofreadingAgent  

### 6. Orchestration
- LangGraph execution graph  
- Deterministic multi-step pipeline  
- State container for final results  

### 7. API Layer
- FastAPI
- Upload endpoint  
- JSON output  
- OpenAPI schema  

---

## Tech Stack

- Python 3.10  
- LangChain  
- LangGraph  
- SentenceTransformers  
- ChromaDB  
- FastAPI  
- Tesseract OCR  
- OpenAI / Anthropic  

---


