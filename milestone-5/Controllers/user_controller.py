"""Controller for user operations.

This module handles user creation and retrieval.
"""

from sqlalchemy.orm import Session
from Repositories import UserRepository
from Schemas.api_schemas import UserResponse


class UserController:
    """Controller for user operations.
    
    Attributes:
        db: SQLAlchemy database session.
        user_repo: Repository for user operations.
    """
    
    def __init__(self, db: Session) -> None:
        """Initialize the user controller.
        
        Args:
            db: SQLAlchemy database session.
        """
        self.db = db
        self.user_repo = UserRepository(db)
    
    def create_user(self, user_name: str) -> UserResponse:
        """Create a new user.
        
        Args:
            user_name: The username for the new user.
            
        Returns:
            UserResponse with user details.
        """
        user = self.user_repo.create(user_name)
        return UserResponse(
            user_id=user.user_id,
            user_name=user.user_name
        )
    
    def get_user(self, user_id: str) -> UserResponse | None:
        """Get a user by ID.
        
        Args:
            user_id: The user's UUID.
            
        Returns:
            UserResponse if found, None otherwise.
        """
        user = self.user_repo.get_by_id(user_id)
        if user:
            return UserResponse(
                user_id=user.user_id,
                user_name=user.user_name
            )
        return None
