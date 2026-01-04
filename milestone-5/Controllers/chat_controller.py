"""Controller for chat operations.

This module handles chat with history and RAG.
"""

from sqlalchemy.orm import Session
from Services.chat_service import ChatService
from Repositories import SessionRepository, UserRepository
from Schemas.api_schemas import ChatResponse


class ChatController:
    """Controller for chat operations.
    
    Attributes:
        db: SQLAlchemy database session.
        chat_service: Service for chat operations.
        session_repo: Repository for session operations.
        user_repo: Repository for user operations.
    """
    
    def __init__(self, db: Session) -> None:
        """Initialize the chat controller.
        
        Args:
            db: SQLAlchemy database session.
        """
        self.db = db
        self.chat_service = ChatService(db)
        self.session_repo = SessionRepository(db)
        self.user_repo = UserRepository(db)
    
    def chat(self, user_id: str, session_id: str, message: str) -> ChatResponse:
        """Process a chat message.
        
        Args:
            user_id: The user's UUID.
            session_id: The session's UUID (optional, creates new if None).
            message: The user's message.
            
        Returns:
            ChatResponse with session_id, answer, and sources.
        """
        # Create session if not exists
        if not session_id:
            session = self.session_repo.create(user_id, title=message[:50])
            session_id = session.session_id
        
        # Process chat
        result = self.chat_service.chat(session_id, message)
        
        return ChatResponse(
            session_id=session_id,
            answer=result["answer"],
            sources=result["sources"]
        )
