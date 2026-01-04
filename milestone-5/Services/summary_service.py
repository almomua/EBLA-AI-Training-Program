"""Summary service for summarizing old chat messages.

This module provides the SummaryService class for message summarization.
"""

from sqlalchemy.orm import Session
from Repositories import MessageRepository, SessionSummaryRepository
from Services.llm_service import LLMService
from Config import settings


class SummaryService:
    """Service for summarizing old chat messages.
    
    Attributes:
        db: SQLAlchemy database session.
        message_repo: Repository for message operations.
        summary_repo: Repository for summary operations.
        llm_service: Service for LLM generation.
    """
    
    def __init__(self, db: Session) -> None:
        """Initialize the summary service.
        
        Args:
            db: SQLAlchemy database session.
        """
        self.db = db
        self.message_repo = MessageRepository(db)
        self.summary_repo = SessionSummaryRepository(db)
        self.llm_service = LLMService()
    
    def summarize_old_messages(self, session_id: str) -> None:
        """Summarize old messages and mark them as inactive.
        
        Args:
            session_id: The session's UUID.
        """
        # Get active messages
        active_messages = self.message_repo.get_active(session_id)
        
        if len(active_messages) <= settings.MAX_HISTORY_MESSAGES:
            return
        
        # Get messages to summarize (keep recent ones active)
        messages_to_summarize = active_messages[:-settings.MAX_HISTORY_MESSAGES]
        
        # Build conversation text
        conversation = []
        for msg in messages_to_summarize:
            conversation.append(f"{msg.role}: {msg.content}")
        conversation_text = "\n".join(conversation)
        
        # Get existing summary
        existing_summary = self.summary_repo.get_by_session(session_id)
        existing_text = existing_summary.summary_text if existing_summary else ""
        
        # Generate new summary
        new_summary = self._generate_summary(existing_text, conversation_text)
        
        # Update or create summary
        total_count = len(messages_to_summarize)
        if existing_summary:
            total_count += existing_summary.messages_count
        
        self.summary_repo.create_or_update(session_id, new_summary, total_count)
        
        # Mark messages as inactive
        message_ids = [msg.message_id for msg in messages_to_summarize]
        self.message_repo.mark_inactive(message_ids)
    
    def _generate_summary(self, existing_summary: str, new_conversation: str) -> str:
        """Generate a summary using the LLM.
        
        Args:
            existing_summary: The existing summary text (if any).
            new_conversation: New conversation to summarize.
            
        Returns:
            The generated summary text.
        """
        return self.llm_service.generate_summary(
            conversation=new_conversation,
            existing_summary=existing_summary if existing_summary else None
        )
