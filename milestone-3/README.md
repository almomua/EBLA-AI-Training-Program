# Milestone 3 – Data Preparation & Indexing

## Learning Objectives
- Preprocess text data, create embeddings, and index documents.
- Expose these operations via FastAPI endpoints.

## Activities
- Prepare dataset (text files, articles, or documents).
- Generate embeddings using a vector store (ChromaDB).
- Build a FastAPI service with endpoints:
  - POST /index → preprocess and index documents.
  - POST /search → accept a query, return relevant documents.

## Deliverables
- [x] A FastAPI project exposing endpoints to index and manage documents.
- [x] Documentation explaining how to call the endpoints and what they return.

---

## Discussion Summary: Data Preparation & Indexing

### 1. What is Document Indexing?
Document indexing is the process of converting documents into searchable vectors (embeddings) stored in a vector database for efficient semantic search.

| Step | What Happens |
|------|-------------|
| **1. Load** | Read file content (PDF, TXT, etc.) |
| **2. Split** | Break into smaller chunks (~1000 chars) |
| **3. Embed** | Convert chunks to vectors using embedding model |
| **4. Store** | Save vectors in ChromaDB for similarity search |

### 2. LangChain
LangChain is a framework for building applications with LLMs. In this milestone, we use it for:
- **Document Loaders**: `PyPDFLoader`, `TextLoader` to read files
- **Text Splitters**: `RecursiveCharacterTextSplitter` to chunk documents
- **Embeddings**: `HuggingFaceEmbeddings` for vector conversion
- **Vector Store**: `Chroma` for storing and searching vectors

### 3. ChromaDB
ChromaDB is an open-source vector database that stores embeddings and enables similarity search.

```python
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-base-en-v1.5")
vectorstore = Chroma.from_documents(chunks, embeddings, persist_directory="storage/chroma_db")
```

### 4. FastAPI Endpoints
The API accepts **two input methods** for indexing:

| Method | Content Type | Use Case |
|--------|--------------|----------|
| **File Upload** | `multipart/form-data` | Upload PDF, TXT files |
| **Raw Text** | `multipart/form-data` | Send text content directly |

Both methods use the same endpoint (`POST /index`) with optional parameters.

---

## API Endpoints

### POST /index
Index a document (file upload OR raw text).

**File Upload:**
```bash
curl -X POST http://localhost:8000/index \
  -F "file=@document.pdf"
```

**Raw Text:**
```bash
curl -X POST http://localhost:8000/index \
  -F "content=This is my document text" \
  -F "source=my_notes.txt"
```

**Response:**
```json
{
  "success": true,
  "message": "Indexed document.pdf",
  "chunks_indexed": 5
}
```

### POST /search
Search indexed documents.

**Request:**
```bash
curl -X POST http://localhost:8000/search \
  -H "Content-Type: application/json" \
  -d '{"query": "What is RAG?", "top_k": 5}'
```

**Response:**
```json
{
  "query": "What is RAG?",
  "results": [
    {
      "content": "RAG (Retrieval-Augmented Generation) combines...",
      "source": "document.pdf",
      "score": 0.85
    }
  ]
}
```

---

## Project Structure (MVCS Pattern)

```
milestone-3/
├── app.py                         # FastAPI entry point
├── Models/
│   └── document_model.py          # Document dataclass
├── Schemas/
│   └── api_schemas.py             # Pydantic request/response models
├── Controllers/
│   ├── index_controller.py        # Indexing logic coordination
│   └── retrieval_controller.py    # Search logic coordination
├── Services/
│   ├── index_service.py           # Document indexing (LangChain + ChromaDB)
│   └── retrieval_service.py       # Document search (ChromaDB)
├── Routes/
│   ├── index_routes.py            # POST /index endpoint
│   └── retrieval_routes.py        # POST /search endpoint
├── Utils/
│   └── file_loader.py             # File loading utility (PDF, TXT)
├── Views/                         # (empty - API responses handled by Schemas)
├── data/                          # Documents to index
├── storage/
│   └── chroma_db/                 # ChromaDB vector store
└── requirements.txt
```

## Files Overview

| File | Description |
|------|-------------|
| `app.py` | FastAPI application entry point |
| `Models/document_model.py` | `DocumentModel` dataclass for document representation |
| `Schemas/api_schemas.py` | Pydantic models for API validation (`IndexResponse`, `SearchRequest`, etc.) |
| `Controllers/index_controller.py` | Coordinates indexing operations |
| `Controllers/retrieval_controller.py` | Coordinates search operations |
| `Services/index_service.py` | Handles embedding generation and ChromaDB storage |
| `Services/retrieval_service.py` | Handles similarity search in ChromaDB |
| `Routes/index_routes.py` | Defines `POST /index` endpoint |
| `Routes/retrieval_routes.py` | Defines `POST /search` endpoint |
| `Utils/file_loader.py` | Loads PDF and TXT files using LangChain loaders |

---

## How to Run

```bash
cd milestone-3
pip install -r requirements.txt
python app.py
```

Or with uvicorn:
```bash
uvicorn app:app --reload
```

API docs available at: `http://localhost:8000/docs`

---

## Resources Used

- [LangChain Documentation](https://python.langchain.com/docs/)
- [ChromaDB Documentation](https://docs.trychroma.com/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)

---

## Notes

- Uses **LangChain** for document loading, splitting, and embedding.
- Uses **ChromaDB** as the vector store for document indexing.
- Uses **HuggingFace embeddings** (BAAI/bge-base-en-v1.5) for vectorization.
- Uses **FastAPI** for REST API endpoints.
- Accepts **both file uploads and raw text** on the same `/index` endpoint.
- Follows the MVCS pattern and Google Python Style Guide.
