"""Repository for SessionSummary database operations.

This module handles all CRUD operations for the SessionSummary model.
"""

from sqlalchemy.orm import Session
from Models.session_summary_model import SessionSummary


class SessionSummaryRepository:
    """Repository for SessionSummary CRUD operations.
    
    Attributes:
        db: SQLAlchemy database session.
    """
    
    def __init__(self, db: Session) -> None:
        """Initialize the repository with a database session.
        
        Args:
            db: SQLAlchemy database session.
        """
        self.db = db
    
    def get_by_session(self, session_id: str) -> SessionSummary | None:
        """Get the summary for a session.
        
        Args:
            session_id: The session's UUID.
            
        Returns:
            The SessionSummary object if found, None otherwise.
        """
        session_data = self.db.query(SessionSummary).filter(
            SessionSummary.session_id == session_id
        ).first()
        return session_data
    
    def create_or_update(self, session_id: str, summary_text: str, messages_count: int) -> SessionSummary:
        """Create or update a session summary.
        
        Args:
            session_id: The session's UUID.
            summary_text: The summary text.
            messages_count: Total number of messages summarized.
            
        Returns:
            The created or updated SessionSummary object.
        """
        summary = self.get_by_session(session_id)
        
        if summary:
            summary.summary_text = summary_text
            summary.messages_count = messages_count
        else:
            summary = SessionSummary(
                session_id=session_id,
                summary_text=summary_text,
                messages_count=messages_count
            )
            self.db.add(summary)
        
        self.db.commit()
        self.db.refresh(summary)
        return summary
