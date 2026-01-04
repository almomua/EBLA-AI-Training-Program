"""Controller for history operations.

This module handles session and message history retrieval.
"""

from sqlalchemy.orm import Session
from Repositories import SessionRepository, MessageRepository
from Schemas.api_schemas import SessionListResponse, HistoryResponse, MessageItem, SessionItem


class HistoryController:
    """Controller for history operations.
    
    Attributes:
        db: SQLAlchemy database session.
        session_repo: Repository for session operations.
        message_repo: Repository for message operations.
    """
    
    def __init__(self, db: Session) -> None:
        """Initialize the history controller.
        
        Args:
            db: SQLAlchemy database session.
        """
        self.db = db
        self.session_repo = SessionRepository(db)
        self.message_repo = MessageRepository(db)
    
    def get_sessions(self, user_id: str) -> SessionListResponse:
        """Get all sessions for a user.
        
        Args:
            user_id: The user's UUID.
            
        Returns:
            SessionListResponse with list of sessions.
        """
        sessions = self.session_repo.get_by_user(user_id)
        session_items = []
        for s in sessions:
            session_items.append(SessionItem(
                session_id=s.session_id,
                title=s.title or "Untitled",
                created_at=s.created_at,
                updated_at=s.updated_at
            ))
        return SessionListResponse(sessions=session_items)
    
    def get_history(self, session_id: str) -> HistoryResponse:
        """Get message history for a session.
        
        Args:
            session_id: The session's UUID.
            
        Returns:
            HistoryResponse with list of messages.
        """
        messages = self.message_repo.get_by_session(session_id)
        message_items = []
        for m in messages:
            message_items.append(MessageItem(
                role=m.role,
                content=m.content,
                created_at=m.created_at
            ))
        return HistoryResponse(session_id=session_id, messages=message_items)
