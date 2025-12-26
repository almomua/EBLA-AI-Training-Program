# Milestone 5 – Chat History, Prompt Engineering & Contextual RAG

## Learning Objectives
- Understand the importance of chat history and context in conversational AI.
- Learn the basics of prompt engineering (instruction design, role prompting, few-shot examples).
- Design and integrate a chat history storage system.
- Enhance the existing RAG bot with context-aware conversations.

## Activities

### 1. Chat History & ERD
- Design an ER Diagram for chat history.
- Define your own table names and structure to store sessions, messages, and context.
- Implement persistence (e.g., SQL DB) for storing user queries, bot responses, and retrieved context.

### 2. Prompt Engineering
- Learn and apply key prompt engineering concepts:
  - **Instruction Prompting**: guide the model with clear instructions.
  - **Role Prompting**: set the assistant's persona.
  - **Few-shot Prompting**: show examples to improve consistency.
- Experiment with rewriting prompts to improve response quality.

### 3. Integration with RAG Bot
- Extend FastAPI endpoints:
  - `POST /chat` → accepts a new user message, stores it, retrieves context from history + RAG, then calls the LLM.
  - `GET /history/{session_id}` → returns the conversation history for a session.
- Ensure the bot responds with context-aware answers, using both history and retrieved documents.

## Deliverables
- [ ] ER Diagram of the chat history database (with custom naming & design).
- [ ] Database implementation for storing chat history.
- [ ] Extended FastAPI endpoints:
  - `POST /chat` (context-aware chat with RAG + history).
  - `GET /history/{session_id}` (retrieve stored history).
- [ ] A short demo or documentation showing:
  - How prompts were engineered and improved.
  - How history + RAG improves the conversation quality.

## Bonus (Optional)
- [ ] Add summarization of old chat history (to keep the context short but relevant).

---

## Notes

*Add your notes and progress here...*

