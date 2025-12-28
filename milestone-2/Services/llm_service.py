# Services/llm_service.py
import ollama
from Models.llm_model import LLMConfig, LLMResponse


class LLMService:
    """Service for interacting with Ollama local LLM."""
    
    def __init__(self, config: LLMConfig) -> None:
        """Initialize the LLM service.
        
        Args:
            config: LLM configuration settings.
        """
        self.config = config
    
    def generate(self, prompt: str) -> LLMResponse:
        """Send a prompt to the LLM and get a response.
        
        Args:
            prompt: The user's question or message.
            
        Returns:
            LLMResponse with the answer.
        """
        response = ollama.chat(
            model=self.config.model_name,
            messages=[{"role": "user", "content": prompt}],
            options={"temperature": self.config.temperature}
        )
        
        return LLMResponse(
            prompt=prompt,
            answer=response["message"]["content"],
            model=response["model"]
        )