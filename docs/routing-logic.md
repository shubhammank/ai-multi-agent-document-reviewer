# Routing Logic Documentation

This document explains how a text chunk is routed to the correct agent.

---

## 1. Rule-Based Routing (YAML)

Example:

"baseline": "evidence"
"improve": "recommendation"
"unclear": "clarification"
"typo": "proofreading"


If any rule matches, routing ends immediately.

---

## 2. Structural Routing

If a chunk is of type `table_row`, it automatically routes to:
evidence


---

## 3. Density Routing

Density score:
density = (#keywords + #numbers) / token_count


Thresholds:
- >0.15 → evidence  
- <0.03 → proofreading  
- otherwise → clarification  

---

## 4. Semantic Similarity Routing

Each category has an "anchor sentence" embedding.

We compute cosine similarity between chunk embedding and category embeddings.

The category with highest similarity wins.

---

## 5. Hybrid Logic (Final Decision)

If density router and semantic router match → use that category.

Else:
- Long chunks → prefer semantic
- Short chunks → prefer density

---

## Final Output

{
"chunk_id": "chunk-8",
"category": "clarification"
}
