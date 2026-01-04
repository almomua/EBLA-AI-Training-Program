"""Chat service for handling conversations with history and RAG.

This module provides the ChatService class for context-aware chat.
"""

from sqlalchemy.orm import Session
from Repositories import MessageRepository, SessionRepository, SessionSummaryRepository
from Services.retrieval_service import RetrievalService
from Services.llm_service import LLMService
from Services.summary_service import SummaryService
from Config import settings


class ChatService:
    """Service for handling chat with history and RAG.
    
    Attributes:
        db: SQLAlchemy database session.
        message_repo: Repository for message operations.
        session_repo: Repository for session operations.
        summary_repo: Repository for summary operations.
        retrieval_service: Service for document retrieval.
        llm_service: Service for LLM generation.
        summary_service: Service for summarization.
    """
    
    def __init__(self, db: Session) -> None:
        """Initialize the chat service.
        
        Args:
            db: SQLAlchemy database session.
        """
        self.db = db
        self.message_repo = MessageRepository(db)
        self.session_repo = SessionRepository(db)
        self.summary_repo = SessionSummaryRepository(db)
        self.retrieval_service = RetrievalService()
        self.llm_service = LLMService()
        self.summary_service = SummaryService(db)
    
    def chat(self, session_id: str, user_message: str) -> dict:
        """Process a chat message and generate a response.
        
        Args:
            session_id: The session's UUID.
            user_message: The user's message.
            
        Returns:
            Dict with answer and sources.
        """
        # 1. Save user message
        self.message_repo.create(session_id, "user", user_message)
        
        # 2. Check if summarization is needed
        active_count = self.message_repo.count_active(session_id)
        if active_count > settings.MAX_HISTORY_MESSAGES:
            self.summary_service.summarize_old_messages(session_id)
        
        # 3. Build context from history + RAG
        context = self._build_context(session_id, user_message)
        
        # 4. Generate response
        answer = self.llm_service.generate(user_message, context)
        
        # 5. Save assistant message
        self.message_repo.create(session_id, "assistant", answer)
        
        # 6. Get sources from RAG results
        rag_results = self.retrieval_service.search(user_message, settings.TOP_K)
        sources = list(set([r["source"] for r in rag_results]))
        
        return {
            "answer": answer,
            "sources": sources
        }
    
    def _build_context(self, session_id: str, query: str) -> list[str]:
        """Build context from chat history and RAG retrieval.
        
        Args:
            session_id: The session's UUID.
            query: The user's query for RAG retrieval.
            
        Returns:
            List of context strings.
        """
        context = []
        
        # Add summary if exists
        summary = self.summary_repo.get_by_session(session_id)
        if summary:
            context.append(f"Previous conversation summary: {summary.summary_text}")
        
        # Add active messages (recent history)
        active_messages = self.message_repo.get_active(session_id)
        for msg in active_messages[-settings.MAX_HISTORY_MESSAGES:]:
            context.append(f"{msg.role}: {msg.content}")
        
        # Add RAG results
        rag_results = self.retrieval_service.search(query, settings.TOP_K)
        for result in rag_results:
            context.append(f"Document: {result['content']}")
        
        return context
