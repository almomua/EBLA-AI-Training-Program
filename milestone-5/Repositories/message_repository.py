"""Repository for Message database operations.

This module handles all CRUD operations for the Message model.
"""

from sqlalchemy.orm import Session
from Models.message_model import Message


class MessageRepository:
    """Repository for Message CRUD operations.
    
    Attributes:
        db: SQLAlchemy database session.
    """
    
    def __init__(self, db: Session) -> None:
        """Initialize the repository with a database session.
        
        Args:
            db: SQLAlchemy database session.
        """
        self.db = db
    
    def create(self, session_id: str, role: str, content: str) -> Message:
        """Create a new message.
        
        Args:
            session_id: The ID of the session this message belongs to.
            role: The role of the sender ("user" or "assistant").
            content: The message content.
            
        Returns:
            The created Message object.
        """
        message = Message(session_id=session_id, role=role, content=content)
        self.db.add(message)
        self.db.commit()
        self.db.refresh(message)
        return message
    
    def get_by_session(self, session_id: str) -> list[Message]:
        """Get all messages for a session.
        
        Args:
            session_id: The session's UUID.
            
        Returns:
            List of all Message objects in the session.
        """
        return self.db.query(Message).filter(Message.session_id == session_id).order_by(Message.created_at).all()
    
    def get_active(self, session_id: str) -> list[Message]:
        """Get active (not summarized) messages for a session.
        
        Args:
            session_id: The session's UUID.
            
        Returns:
            List of active Message objects.
        """
        return self.db.query(Message).filter(
            Message.session_id == session_id,
            Message.is_active == True
        ).order_by(Message.created_at).all()
    
    def mark_inactive(self, message_ids: list[int]) -> int:
        """Mark messages as inactive (summarized).
        
        Args:
            message_ids: List of message IDs to mark as inactive.
            
        Returns:
            Number of messages updated.
        """
        count = self.db.query(Message).filter(
            Message.message_id.in_(message_ids)
        ).update({"is_active": False}, synchronize_session=False)
        self.db.commit()
        return count
    
    def count_active(self, session_id: str) -> int:
        """Count active messages in a session.
        
        Args:
            session_id: The session's UUID.
            
        Returns:
            Number of active messages.
        """
        return self.db.query(Message).filter(
            Message.session_id == session_id,
            Message.is_active == True
        ).count()
