"""Session summary model for storing conversation summaries.

This module defines the SessionSummary ORM model for the chat application.
"""

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from Database import Base


class SessionSummary(Base):
    """SessionSummary model representing a summary of old messages.
    
    Attributes:
        summary_id: Unique identifier for the summary (auto-increment).
        session_id: Foreign key to the session (unique - one summary per session).
        summary_text: The summarized text of old messages.
        messages_count: Number of messages that have been summarized.
        updated_at: Timestamp when the summary was last updated.
        session: The session this summary belongs to.
    """
    __tablename__ = "session_summaries"
    
    summary_id = Column(Integer, primary_key=True, autoincrement=True)
    session_id = Column(String, ForeignKey("sessions.session_id"), unique=True, nullable=False)
    summary_text = Column(Text, nullable=False)
    messages_count = Column(Integer, default=0)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    session = relationship("Session", back_populates="summary")
