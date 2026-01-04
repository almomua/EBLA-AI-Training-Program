"""Routes for history operations.

This module defines session and history endpoints.
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from Database import get_db
from Controllers.history_controller import HistoryController
from Schemas.api_schemas import SessionListResponse, HistoryResponse

router = APIRouter()


@router.get("/sessions/{user_id}", response_model=SessionListResponse)
def get_sessions(user_id: str, db: Session = Depends(get_db)):
    """Get all sessions for a user.
    
    Args:
        user_id: The user's UUID.
        db: Database session (injected).
        
    Returns:
        SessionListResponse with list of sessions.
    """
    controller = HistoryController(db)
    return controller.get_sessions(user_id)


@router.get("/history/{session_id}", response_model=HistoryResponse)
def get_history(session_id: str, db: Session = Depends(get_db)):
    """Get message history for a session.
    
    Args:
        session_id: The session's UUID.
        db: Database session (injected).
        
    Returns:
        HistoryResponse with list of messages.
    """
    controller = HistoryController(db)
    return controller.get_history(session_id)
