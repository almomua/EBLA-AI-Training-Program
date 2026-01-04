"""Routes for chat operations.

This module defines the chat endpoint.
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from Database import get_db
from Controllers.chat_controller import ChatController
from Schemas.api_schemas import ChatRequest, ChatResponse

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest, db: Session = Depends(get_db)):
    """Send a message and get a response with history context.
    
    Args:
        request: ChatRequest with user_id, session_id, and message.
        db: Database session (injected).
        
    Returns:
        ChatResponse with session_id, answer, and sources.
    """
    controller = ChatController(db)
    return controller.chat(request.user_id, request.session_id, request.message)
