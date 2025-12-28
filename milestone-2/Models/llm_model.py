# Models/llm_model.py
from dataclasses import dataclass

@dataclass
class LLMConfig:
    """Configuration for connecting to Ollama local LLM.
    
    Attributes:
        model_name: The Ollama model to use 
        temperature: Controls randomness 
    """
    model_name: str = "gemma3:1b"
    temperature: float = 0.7


@dataclass
class LLMResponse:
    """Structured response from the LLM.
    
    Attributes:
        prompt: The user's original question.
        answer: The LLM's generated response.
        model: Which model generated the response.
    """
    prompt: str
    answer: str
    model: str