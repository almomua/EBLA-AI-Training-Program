# Controllers/rag_controller.py
from Models.llm_model import LLMConfig
from Services.llm_service import LLMService
from Services.index_service import IndexService
from Views.chat_viewer import ChatViewer


class RAGController:
    """Coordinates user requests between services and views."""
    
    def __init__(self, data_dir: str = "./data", model_name: str = "gemma3:1b", embed_model_name: str = "BAAI/bge-base-en-v1.5") -> None:
        """Initialize controller with services and view.
        
        Args:
            data_dir: Path to documents folder.
            model_name: Ollama model to use for generation.
            embed_model_name: HuggingFace model to use for embeddings.
        """
        # Initialize dependencies
        config = LLMConfig(model_name=model_name, temperature=0.7)
        self.llm_service = LLMService(config)
        self.index_service = IndexService(data_dir, model_name, embed_model_name)
        self.view = ChatViewer()
    
    def chat(self, prompt: str) -> None:
        """Handle direct chat with LLM (no retrieval).
        
        Args:
            prompt: User's message.
        """
        try:
            response = self.llm_service.generate(prompt)
            self.view.display_llm_response(response)
        except Exception as e:
            self.view.display_error(str(e))
    
    def index_documents(self) -> None:
        """Handle document indexing request."""
        try:
            count = self.index_service.load_and_index()
            self.view.display_index_success(count)
        except Exception as e:
            self.view.display_error(str(e))
    
    def query(self, question: str) -> None:
        """Handle RAG query (retrieve + generate).
        
        Args:
            question: User's question about the documents.
        """
        try:
            answer = self.index_service.query(question)
            self.view.display_query_result(question, answer)
        except Exception as e:
            self.view.display_error(str(e))