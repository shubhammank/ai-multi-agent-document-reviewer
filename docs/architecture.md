# System Architecture Overview

This document explains how the system works end-to-end.

---

## 1. Ingestion Layer

Modules:
- PDFReader
- DOCXReader
- OCREngine

This layer:
- Extracts text + layout elements
- Normalizes metadata
- Produces raw structured chunks

---

## 2. Chunking Layer

Steps:
1. Clean text  
2. Add density score  
3. Detect boundaries  
4. Hybrid semantic chunking  
5. Build context windows  
6. Normalize final chunk objects  

---

## 3. Embedding Layer

Uses:
- SentenceTransformer
- Optional OpenAI embeddings

Stores vectors in ChromaDB.

Delta embedding logic ensures we avoid recomputing embeddings when a file hasn't changed.

---

## 4. Routing Layer

The Router uses:
- YAML keyword rules
- DensityRouter
- SemanticRouter
- Structure-based rules

Final category is selected via hybrid scoring logic.

---

## 5. Multi-Agent Layer

Agents:
- RecommendationAgent
- EvidenceAgent
- ClarificationAgent
- ProofreadingAgent

Each agent uses:
- Shared LLM call wrapper (AgentBase)
- Structured JSON output
- System prompt specialization

---

## 6. LangGraph Orchestration

Pipeline steps:

ingest → chunk → embed → route → agents → merge → END

---

## 7. API Layer

FastAPI app exposes:

- POST /review  
- GET /health  

---
