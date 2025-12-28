# Services/index_service.py
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, Settings
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding


class IndexService:
    """Service for indexing and querying documents using Ollama."""
    
    def __init__(
        self, 
        data_dir: str = "./data",
        model_name: str = "gemma3:1b",
        embed_model_name: str = "all-MiniLM-L6-v2"
    ) -> None:
        """Initialize the index service with Ollama as the LLM.
        
        Args:
            data_dir: Path to folder containing documents.
            model_name: Ollama model to use for generation.
            embed_model_name: HuggingFace model to use for embeddings.
        """
        self.data_dir = data_dir
        self.index = None
        
        # Configure LlamaIndex to use Ollama for LLM and embeddings
        Settings.llm = Ollama(model=model_name, request_timeout=120.0)
        Settings.embed_model = HuggingFaceEmbedding(model_name=embed_model_name)
    
    def load_and_index(self) -> int:
        """Load documents and create vector index.
        
        Returns:
            Number of documents indexed.
        """
        documents = SimpleDirectoryReader(self.data_dir).load_data()
        self.index = VectorStoreIndex.from_documents(documents , embed_model=Settings.embed_model)
        return len(documents)
    
    def query(self, question: str) -> str:
        """Query the index with a question.
        
        Args:
            question: The question to ask.
            
        Returns:
            The answer from the index.
            
        Raises:
            ValueError: If index hasn't been built yet.
        """
        if self.index is None:
            raise ValueError("Index not built. Call load_and_index() first.")
        
        query_engine = self.index.as_query_engine(
            llm=Settings.llm,
        )
        response = query_engine.query(question)
        return str(response)