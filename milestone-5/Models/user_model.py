"""User model for storing user information.

This module defines the User ORM model for the chat application.
"""

from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from Database import Base
from Utils import generate_uuid


class User(Base):
    """User model representing a chat application user.
    
    Attributes:
        user_id: Unique identifier for the user (UUID).
        user_name: Unique username for the user.
        created_at: Timestamp when the user was created.
        sessions: List of chat sessions belonging to the user.
    """
    __tablename__ = "users"
    
    user_id = Column(String, primary_key=True, default=generate_uuid)
    user_name = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    sessions = relationship("Session", back_populates="user")
