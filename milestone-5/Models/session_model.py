"""Session model for storing chat sessions.

This module defines the Session ORM model for the chat application.
"""

from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from Database import Base
from Utils import generate_uuid


class Session(Base):
    """Session model representing a chat conversation.
    
    Attributes:
        session_id: Unique identifier for the session (UUID).
        user_id: Foreign key to the user who owns this session.
        title: Optional title for the session.
        created_at: Timestamp when the session was created.
        updated_at: Timestamp when the session was last updated.
        user: The user who owns this session.
        messages: List of messages in this session.
        summary: Summary of the session (one-to-one relationship).
    """
    __tablename__ = "sessions"
    
    session_id = Column(String, primary_key=True, default=generate_uuid)
    user_id = Column(String, ForeignKey("users.user_id"), nullable=False)
    title = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    user = relationship("User", back_populates="sessions")
    messages = relationship("Message", back_populates="session")
    summary = relationship("SessionSummary", back_populates="session", uselist=False)
