from pydantic import BaseModel


# ============ INDEX ENDPOINT ============

class IndexTextRequest(BaseModel):
    """Request for indexing raw text content."""
    content: str
    source: str  # filename or identifier


class IndexResponse(BaseModel):
    """Response for POST /index (both text and file upload)."""
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
    top_k: int = 3  # Number of documents to retrieve for context


class AskResponse(BaseModel):
    """Response for POST /ask."""
    query: str
    answer: str
    sources: list[str]  # Source documents used
