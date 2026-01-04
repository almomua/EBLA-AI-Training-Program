"""Pydantic schemas for API request/response validation.

This module defines all Pydantic models for the API endpoints.
"""

from pydantic import BaseModel
from datetime import datetime
from typing import Optional


# ============ INDEX ENDPOINT ============

class IndexTextRequest(BaseModel):
    """Request for indexing raw text content."""
    content: str
    source: str


class IndexResponse(BaseModel):
    """Response for POST /index."""
    success: bool
    message: str
    chunks_indexed: int


# ============ SEARCH ENDPOINT ============

class SearchRequest(BaseModel):
    """Request for POST /search."""
    query: str
    top_k: int = 5


class SearchResult(BaseModel):
    """Single search result."""
    content: str
    source: str
    score: float


class SearchResponse(BaseModel):
    """Response for POST /search."""
    query: str
    results: list[SearchResult]


# ============ ASK ENDPOINT ============

class AskRequest(BaseModel):
    """Request for POST /ask."""
    query: str
    top_k: int = 3


class AskResponse(BaseModel):
    """Response for POST /ask."""
    query: str
    answer: str
    sources: list[str]


# ============ USER ENDPOINTS ============

class CreateUserRequest(BaseModel):
    """Request for POST /users."""
    user_name: str


class UserResponse(BaseModel):
    """Response for user operations."""
    user_id: str
    user_name: str


# ============ CHAT ENDPOINT ============

class ChatRequest(BaseModel):
    """Request for POST /chat."""
    user_id: str
    session_id: Optional[str] = None
    message: str


class ChatResponse(BaseModel):
    """Response for POST /chat."""
    session_id: str
    answer: str
    sources: list[str]


# ============ HISTORY ENDPOINTS ============

class SessionItem(BaseModel):
    """Single session item."""
    session_id: str
    title: str
    created_at: datetime
    updated_at: datetime


class SessionListResponse(BaseModel):
    """Response for GET /sessions/{user_id}."""
    sessions: list[SessionItem]


class MessageItem(BaseModel):
    """Single message item."""
    role: str
    content: str
    created_at: datetime


class HistoryResponse(BaseModel):
    """Response for GET /history/{session_id}."""
    session_id: str
    messages: list[MessageItem]
