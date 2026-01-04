"""FastAPI application entry point.

This module initializes the FastAPI app and registers all routes.
"""
from Config import settings
from fastapi import FastAPI
from Database import init_db
from Routes import (
    index_router,
    retrieval_router,
    ask_router,
    chat_router,
    user_router,
    history_router,
)

app = FastAPI(title="RAG Chat API", version="1.0.0")

# Register routes
app.include_router(index_router, tags=["Index"], prefix="/api/v1")
app.include_router(retrieval_router, tags=["Search"], prefix="/api/v1")
app.include_router(ask_router, tags=["Ask"], prefix="/api/v1")
app.include_router(chat_router, tags=["Chat"], prefix="/api/v1")
app.include_router(user_router, tags=["Users"], prefix="/api/v1")
app.include_router(history_router, tags=["History"], prefix="/api/v1")


@app.on_event("startup")
def startup():
    """Initialize database tables on startup."""
    init_db()


@app.get("/")
def root():
    """Health check endpoint."""
    return {"message": "RAG Chat API - Milestone 5"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
