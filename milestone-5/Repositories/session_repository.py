"""Repository for Session database operations.

This module handles all CRUD operations for the Session model.
"""

from sqlalchemy.orm import Session as DbSession
from Models.session_model import Session


class SessionRepository:
    """Repository for Session CRUD operations.
    
    Attributes:
        db: SQLAlchemy database session.
    """
    
    def __init__(self, db: DbSession) -> None:
        """Initialize the repository with a database session.
        
        Args:
            db: SQLAlchemy database session.
        """
        self.db = db
    
    def create(self, user_id: str, title: str = None) -> Session:
        """Create a new chat session.
        
        Args:
            user_id: The ID of the user who owns this session.
            title: Optional title for the session.
            
        Returns:
            The created Session object.
        """
        session = Session(user_id=user_id, title=title)
        self.db.add(session)
        self.db.commit()
        self.db.refresh(session)
        return session
    
    def get_by_id(self, session_id: str) -> Session | None:
        """Get a session by its ID.
        
        Args:
            session_id: The session's UUID.
            
        Returns:
            The Session object if found, None otherwise.
        """
        return self.db.query(Session).filter(Session.session_id == session_id).first()
    
    def get_by_user(self, user_id: str) -> list[Session]:
        """Get all sessions for a user.
        
        Args:
            user_id: The user's UUID.
            
        Returns:
            List of Session objects belonging to the user.
        """
        return self.db.query(Session).filter(Session.user_id == user_id).order_by(Session.updated_at.desc()).all()
    
    def update_title(self, session_id: str, title: str) -> Session | None:
        """Update the title of a session.
        
        Args:
            session_id: The session's UUID.
            title: The new title.
            
        Returns:
            The updated Session object if found, None otherwise.
        """
        session = self.get_by_id(session_id)
        if session:
            session.title = title
            self.db.commit()
            self.db.refresh(session)
        return session
