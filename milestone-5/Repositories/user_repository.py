"""Repository for User database operations.

This module handles all CRUD operations for the User model.
"""

from sqlalchemy.orm import Session
from Models.user_model import User


class UserRepository:
    """Repository for User CRUD operations.
    
    Attributes:
        db: SQLAlchemy database session.
    """
    
    def __init__(self, db: Session) -> None:
        """Initialize the repository with a database session.
        
        Args:
            db: SQLAlchemy database session.
        """
        self.db = db
    
    def create(self, user_name: str) -> User:
        """Create a new user.
        
        Args:
            user_name: Unique username for the user.
            
        Returns:
            The created User object.
        """
        user = User(user_name=user_name)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def get_by_id(self, user_id: str) -> User | None:
        """Get a user by their ID.
        
        Args:
            user_id: The user's UUID.
            
        Returns:
            The User object if found, None otherwise.
        """
        return self.db.query(User).filter(User.user_id == user_id).first()
    
    def get_by_username(self, user_name: str) -> User | None:
        """Get a user by their username.
        
        Args:
            user_name: The user's username.
            
        Returns:
            The User object if found, None otherwise.
        """
        return self.db.query(User).filter(User.user_name == user_name).first()
