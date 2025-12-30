# Milestone 4 – Retrieval & LLM Integration

## Learning Objectives
- Implement retrieval of relevant documents.
- Integrate retrieval results with the local LLM to generate responses.
- Expose functionality via FastAPI.

## Activities
- Add a retrieval pipeline that fetches documents based on a query.
- Pass retrieved documents to LLM for response generation.
- Extend FastAPI with:
  - POST /ask → accept a query, retrieve documents, and generate an LLM response.

## Deliverables
- [x] A FastAPI project with working endpoints for document retrieval and LLM integration.
- [x] Example cURL or Postman requests demonstrating usage.

---

## Discussion Summary: Retrieval & LLM Integration

### 1. What is RAG (Retrieval-Augmented Generation)?
RAG combines document retrieval with LLM generation to produce accurate, context-aware responses.

| Step | What Happens |
|------|-------------|
| **1. Query** | User asks a question |
| **2. Retrieve** | Search ChromaDB for relevant document chunks |
| **3. Augment** | Build prompt with retrieved context |
| **4. Generate** | LLM generates answer using context |

### 2. LLM Integration (Ollama)
Ollama runs language models locally without API costs.

```bash
ollama pull gemma3:1b
ollama serve
```

```python
from langchain_ollama import ChatOllama

llm = ChatOllama(model="gemma3:1b")
response = llm.invoke(prompt)
answer = response.content
```

### 3. Prompt Engineering
The prompt template guides the LLM to use the retrieved context:

```
Use the following context to answer the question.
If the answer is not in the context, say "I don't have enough information."

Context:
{retrieved_chunks}

Question: {user_query}

Answer:
```

---

## API Endpoints

### POST /index
Index a document (file upload OR raw text).

```bash
curl -X POST http://localhost:8000/index \
  -F "file=@document.pdf"
```

### POST /search
Search indexed documents.

```bash
curl -X POST http://localhost:8000/search \
  -H "Content-Type: application/json" \
  -d '{"query": "What is RAG?", "top_k": 5}'
```

### POST /ask
Ask a question and get an LLM-generated answer using RAG.

```bash
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"query": "What is RAG?", "top_k": 3}'
```

---

## Project Structure (MVCS Pattern)

```
milestone-4/
├── app.py                         # FastAPI entry point
├── Models/
│   └── document_model.py          # Document dataclass
├── Schemas/
│   └── api_schemas.py             # Pydantic request/response models
├── Controllers/
│   ├── index_controller.py        # Indexing logic
│   ├── retrieval_controller.py    # Search logic
│   └── ask_controller.py          # RAG Q&A logic
├── Services/
│   ├── index_service.py           # Document indexing (ChromaDB)
│   ├── retrieval_service.py       # Document search (ChromaDB)
│   └── llm_service.py             # Ollama LLM integration
├── Routes/
│   ├── index_routes.py            # POST /index
│   ├── retrieval_routes.py        # POST /search
│   └── ask_routes.py              # POST /ask
├── Utils/
│   └── file_loader.py             # File loading utility
├── Views/
├── data/                          # Documents to index
├── storage/
│   └── chroma_db/                 # ChromaDB vector store
└── requirements.txt
```

## Files Overview

| File | Description |
|------|-------------|
| `app.py` | FastAPI application entry point |
| `Models/document_model.py` | `DocumentModel` dataclass |
| `Schemas/api_schemas.py` | Pydantic models (`AskRequest`, `AskResponse`, etc.) |
| `Controllers/ask_controller.py` | Coordinates RAG Q&A (retrieve + generate) |
| `Services/llm_service.py` | Ollama LLM interaction |
| `Routes/ask_routes.py` | `POST /ask` endpoint |

---

## Demo Output

Using `EBLA-AI-Training-Phase1.pdf` as the indexed document:

**Request:**
```bash
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"query": "What are the milestones in the training program?", "top_k": 3}'
```

**Response:**
```json
{
  "query": "What are the milestones in the training program?",
  "answer": "The training program consists of 6 milestones: Milestone 1 covers Python basics, Milestone 2 focuses on RAG and Core Technologies, Milestone 3 covers Data Preparation and Indexing, Milestone 4 handles Retrieval and LLM Integration, Milestone 5 adds Chat History and Prompt Engineering, and Milestone 6 is for Optimization and Finalization.",
  "sources": ["EBLA-AI-Training-Phase1.pdf"]
}
```

**Another example:**
```bash
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"query": "What should I learn in Milestone 3?", "top_k": 3}'
```

**Response:**
```json
{
  "query": "What should I learn in Milestone 3?",
  "answer": "In Milestone 3, you should learn to preprocess text data, create embeddings, and index documents. You will also expose these operations via FastAPI endpoints including POST /index to preprocess and index documents, and POST /search to accept a query and return relevant documents.",
  "sources": ["EBLA-AI-Training-Phase1.pdf"]
}
```

---

## How to Run

1. Start Ollama:
```bash
ollama serve
```

2. Run the API:
```bash
cd milestone-4
pip install -r requirements.txt
python app.py
```

API docs available at: `http://localhost:8000/docs`

---

## Resources Used

- [LangChain Documentation](https://python.langchain.com/docs/)
- [LangChain Ollama Integration](https://python.langchain.com/docs/integrations/llms/ollama/)
- [ChromaDB Documentation](https://docs.trychroma.com/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Ollama Documentation](https://ollama.ai/)

---

## Notes

- Uses **Ollama** (gemma3:1b) as the local LLM for response generation.
- Uses **LangChain** for document loading, splitting, embedding, and LLM integration.
- Uses **ChromaDB** as the vector store for document indexing and retrieval.
- Uses **HuggingFace embeddings** (BAAI/bge-base-en-v1.5) for vectorization.
- Uses **FastAPI** for REST API endpoints.
- Follows the MVCS pattern and Google Python Style Guide.
