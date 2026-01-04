"""Routes module for FastAPI endpoint definitions."""

from Routes.index_routes import router as index_router
from Routes.retrieval_routes import router as retrieval_router
from Routes.ask_routes import router as ask_router
from Routes.chat_routes import router as chat_router
from Routes.user_routes import router as user_router
from Routes.history_routes import router as history_router
