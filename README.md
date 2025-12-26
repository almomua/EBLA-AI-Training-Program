# EBLA AI Trainee Program – Phase 1

This repository contains my work and progress for the **EBLA AI Trainee Program – Phase 1**.  
The goal of this phase is to build a complete **Retrieval-Augmented Generation (RAG)** system, starting from Python basics and ending with a functional API-based AI assistant.

---

## Milestones

| Milestone | Description | Link |
|-----------|-------------|------|
| **Milestone 1** | Python Basics | [View →](./milestone-1/README.md) |
| **Milestone 2** | RAG & Core Technologies | [View →](./milestone-2/README.md) |
| **Milestone 3** | Data Preparation & Indexing | [View →](./milestone-3/README.md) |
| **Milestone 4** | Retrieval & LLM Integration | [View →](./milestone-4/README.md) |
| **Milestone 5** | Chat History & Contextual RAG | [View →](./milestone-5/README.md) |
| **Milestone 6** | Optimization & Finalization | [View →](./milestone-6/README.md) |

---

## Milestone Details

### [Milestone 1 – Python Basics](./milestone-1/)
Learn and practice core Python concepts (variables, data types, control flow, functions, classes) and write clean, well-structured code.

### [Milestone 2 – RAG & Core Technologies](./milestone-2/)
Understand RAG architecture and experiment with a local LLM and an indexing library (e.g., LlamaIndex or LangChain).

### [Milestone 3 – Data Preparation & Indexing](./milestone-3/)
Prepare text data, create embeddings with a vector store (e.g., FAISS, ChromaDB), and expose indexing/search via FastAPI endpoints.

### [Milestone 4 – Retrieval & LLM Integration](./milestone-4/)
Implement document retrieval and integrate it with the local LLM through FastAPI (e.g., `/ask` endpoint).

### [Milestone 5 – Chat History & Contextual RAG](./milestone-5/)
Design a chat history database, apply prompt engineering techniques, and build context-aware chat endpoints (e.g., `/chat`, `/history/{session_id}`).

### [Milestone 6 – Optimization & Finalization](./milestone-6/)
Optimize performance, test with multiple datasets, and prepare a demo of the end-to-end RAG system.

---

## Repository Structure

```
EBLA-Training-Program/
├── README.md
├── milestone-1/
│   └── README.md
├── milestone-2/
│   └── README.md
├── milestone-3/
│   └── README.md
├── milestone-4/
│   └── README.md
├── milestone-5/
│   └── README.md
└── milestone-6/
    └── README.md
```

---

## Notes

- The project follows **MVC principles** where applicable.
- Code is written following the **Google Python Style Guide** (type hints, docstrings, naming conventions).
- Each milestone has **separate commits** and documentation to track progress clearly.
