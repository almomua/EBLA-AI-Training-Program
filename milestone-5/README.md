# Milestone 5 – Chat History, Prompt Engineering & Contextual RAG

## Learning Objectives
- Understand the importance of chat history and context in conversational AI.
- Learn the basics of prompt engineering (instruction design, role prompting).
- Design and integrate a chat history storage system.
- Enhance the existing RAG bot with context-aware conversations.

## Activities
- Design an ER Diagram for chat history.
- Implement persistence (PostgreSQL) for storing user queries, bot responses, and context.
- Extend FastAPI endpoints:
  - POST /chat → accepts a new user message, stores it, retrieves context from history + RAG, then calls the LLM.
  - GET /history/{session_id} → returns the conversation history for a session.

## Deliverables
- [x] ER Diagram of the chat history database.
- [x] Database implementation for storing chat history.
- [x] Extended FastAPI endpoints (POST /chat, GET /history, GET /sessions).
- [x] Context-aware chat with RAG + history.

---

## ER Diagram

<!-- TODO: Add your ERD image here -->
![Chat History Database ERD](./erd-diagram.png)

---

## Discussion Summary: Chat History & Contextual RAG

### 1. ChatGPT-like Context Window
The system uses a context window approach where:
- Recent messages stay **active** in context
- Old messages get **summarized** by the LLM
- Summary + active messages + RAG = full context

| Component | Purpose |
|-----------|---------|
| **Active Messages** | Recent conversation (last N messages) |
| **Summary** | Compressed history of old messages |
| **RAG Results** | Relevant document chunks |

### 2. Database Design
Four tables store the chat data:

| Table | Purpose |
|-------|---------|
| `users` | Store user accounts |
| `sessions` | Store chat sessions per user |
| `messages` | Store messages with `is_active` flag |
| `session_summaries` | Store one summary per session |

### 3. Summarization Flow
When active messages exceed the limit:

```
1. Count active messages
2. If count > MAX_HISTORY_MESSAGES:
   - Get oldest active messages
   - Summarize with LLM
   - Update session summary
   - Mark old messages as inactive
```

### 4. Context Building
For each chat request:

```
Context = [
    Summary (if exists),
    Active messages (recent history),
    RAG results (relevant documents)
]
```

---

## API Endpoints

### POST /api/v1/users
Create a new user.

```bash
curl -X POST http://localhost:8000/api/v1/users \
  -H "Content-Type: application/json" \
  -d '{"user_name": "john"}'
```

### POST /api/v1/chat
Send a message with history context.

```bash
curl -X POST http://localhost:8000/api/v1/chat \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "abc-123",
    "session_id": null,
    "message": "What is RAG?"
  }'
```

**Response:**
```json
{
  "session_id": "xyz-456",
  "answer": "RAG (Retrieval-Augmented Generation) is...",
  "sources": ["document.pdf"]
}
```

### GET /api/v1/sessions/{user_id}
Get all sessions for a user.

```bash
curl http://localhost:8000/api/v1/sessions/abc-123
```

### GET /api/v1/history/{session_id}
Get message history for a session.

```bash
curl http://localhost:8000/api/v1/history/xyz-456
```

---

## Project Structure

```
milestone-5/
├── app.py                         # FastAPI entry point
├── .env                           # Environment variables
│
├── Config/
│   └── settings.py                # App configuration
│
├── Database/
│   └── database.py                # SQLAlchemy connection
│
├── Models/
│   ├── user_model.py              # User ORM
│   ├── session_model.py           # Session ORM
│   ├── message_model.py           # Message ORM
│   └── session_summary_model.py   # Summary ORM
│
├── Repositories/
│   ├── user_repository.py         # User CRUD
│   ├── session_repository.py      # Session CRUD
│   ├── message_repository.py      # Message CRUD
│   └── session_summary_repository.py
│
├── Schemas/
│   └── api_schemas.py             # Pydantic models
│
├── Services/
│   ├── index_service.py           # Document indexing
│   ├── retrieval_service.py       # Document search
│   ├── llm_service.py             # Ollama LLM
│   ├── chat_service.py            # Chat with history
│   └── summary_service.py         # Message summarization
│
├── Controllers/
│   ├── chat_controller.py         # Chat logic
│   ├── user_controller.py         # User logic
│   └── history_controller.py      # History logic
│
├── Routes/
│   ├── chat_routes.py             # POST /chat
│   ├── user_routes.py             # User endpoints
│   └── history_routes.py          # History endpoints
│
├── Utils/
│   ├── file_loader.py             # File loading
│   └── id_generator.py            # UUID generation
│
└── storage/
    └── chroma_db/                 # ChromaDB vector store
```

## Files Overview

| File | Description |
|------|-------------|
| `Config/settings.py` | App configuration (DB, LLM, RAG settings) |
| `Database/database.py` | SQLAlchemy engine and session |
| `Models/*.py` | ORM models for users, sessions, messages, summaries |
| `Repositories/*.py` | Database CRUD operations |
| `Services/chat_service.py` | Chat with history + RAG |
| `Services/summary_service.py` | Summarize old messages |
| `Routes/chat_routes.py` | POST /chat endpoint |
| `Routes/history_routes.py` | GET /sessions, GET /history endpoints |

---

## How to Run

1. Start PostgreSQL and create database:
```sql
CREATE DATABASE rag_chat;
```

2. Configure `.env`:
```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=rag_chat
DB_USER=postgres
DB_PASSWORD=your_password
```

3. Start Ollama:
```bash
ollama serve
```

4. Run the API:
```bash
cd milestone-5
pip install -r requirements.txt
python app.py
```

API docs available at: `http://localhost:8000/docs`

---

## Resources Used

- [LangChain Documentation](https://python.langchain.com/docs/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Pydantic Settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)

---

## Notes

- Uses **PostgreSQL** for chat history persistence.
- Uses **ChatGPT-like context window** (summary + recent messages).
- Uses **Ollama** (gemma3:1b) for LLM generation.
- Uses **ChromaDB** for document vector storage.
- Automatically **summarizes old messages** when history exceeds limit.
- Follows the MVCS pattern with Repository layer.
- Follows Google Python Style Guide.
