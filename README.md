# Multi-Agent Document Reviewer

This project implements a multi-agent AI system that reviews PDF and DOCX documents and generates four categories of comments: Recommendations, Evidence, Clarifications, and Proofreading. The pipeline uses semantic chunking, configurable routing rules, vector search, and delta-based embedding updates.

## Features
- Multi-agent architecture using LangGraph or CrewAI
- Semantic chunking with YAML configuration
- Vector database retrieval (FAISS or ChromaDB)
- Delta embedding refresh using hashing
- Support for PDF, DOCX, and OCR text extraction
- Four comment clusters generated independently
- Full REST API specification included
- Notebook experiments for chunking, routing, and evaluation

## Architecture Overview
1. Document ingestion (PDF and DOCX readers)
2. Semantic chunking and metadata tagging
3. Embedding creation and storage in vector DB
4. Routing engine assigns chunks to agents
5. Agents generate comments per cluster
6. Orchestrator merges, deduplicates, and formats results
7. API exposes review endpoint

Refer to docs/architecture.md for diagrams and extended details.

## Project Structure
- src: Core application logic
- agents: Individual agent modules
- config: YAML configurations
- docs: Architecture, flow and design notes
- api: OpenAPI specification and API server
- notebooks: Experiments and prototype tests
- tests: Unit tests
