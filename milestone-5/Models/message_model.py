"""Message model for storing chat messages.

This module defines the Message ORM model for the chat application.
"""

from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from Database import Base


class Message(Base):
    """Message model representing a single chat message.
    
    Attributes:
        message_id: Unique identifier for the message (auto-increment).
        session_id: Foreign key to the session this message belongs to.
        role: The role of the message sender ("user" or "assistant").
        content: The text content of the message.
        is_active: Whether the message is active in context (True) or summarized (False).
        created_at: Timestamp when the message was created.
        session: The session this message belongs to.
    """
    __tablename__ = "messages"
    
    message_id = Column(Integer, primary_key=True, autoincrement=True)
    session_id = Column(String, ForeignKey("sessions.session_id"), nullable=False)
    role = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    session = relationship("Session", back_populates="messages")
