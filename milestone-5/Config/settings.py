from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # App
    APP_NAME: str = None
    APP_VERSION: str = None
    DEBUG: bool = None
    
    # Database (PostgreSQL)
    DB_HOST: str = None
    DB_PORT: int = None
    DB_NAME: str = None
    DB_USER: str = None
    DB_PASSWORD: str = None
       
    # ChromaDB
    CHROMA_PERSIST_DIR: str = None
    
    # Embeddings
    EMBED_MODEL: str = None
    
    # LLM (Ollama)
    LLM_MODEL: str = None
    LLM_TEMPERATURE: float = None
    
    # RAG
    CHUNK_SIZE: int = None
    CHUNK_OVERLAP: int = None
    TOP_K: int = None
    
    # Chat
    MAX_HISTORY_MESSAGES: int = None
    SUMMARIZE_AFTER: int = None
    
    class Config:
        env_file = ".env"


settings = Settings()