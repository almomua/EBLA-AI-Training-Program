"""LLM Service for generating responses using Ollama."""

from langchain_ollama import ChatOllama
from Config import settings


class LLMService:
    """Service for interacting with Ollama LLM."""
    
    def __init__(self, model_name: str = None):
        """Initialize the LLM service."""
        model = model_name or settings.LLM_MODEL
        self.llm = ChatOllama(
            model=model,
            temperature=settings.LLM_TEMPERATURE
        )
    
    def generate(self, query: str, context: list[str]) -> str:
        """Generate a response using context.
        
        Args:
            query: User's question.
            context: Chat history and retrieved documents.
        
        Returns:
            LLM generated answer.
        """
        context_text = "\n".join(context) if context else ""
        print(context_text)
        
        prompt = f"""You are an AI assistant for Ebla company.

Use the information below to answer the question:
- Check CHAT HISTORY for previous conversation
- Check DOCUMENTS for company information
- Answer naturally for simple questions

{context_text}

Question: {query}
Answer:"""
        
        response = self.llm.invoke(prompt)
        return response.content
    
    def generate_summary(self, conversation: str, existing_summary: str = None) -> str:
        """Generate a summary of conversation.
        
        Args:
            conversation: The conversation to summarize.
            existing_summary: Previous summary to update.
        
        Returns:
            Concise summary.
        """
        if existing_summary:
            prompt = f"""Update this summary with new conversation:

Previous: {existing_summary}
New: {conversation}

Updated summary (2 sentences):"""
        else:
            prompt = f"""Summarize this conversation (2 sentences):

{conversation}

Summary:"""
        
        response = self.llm.invoke(prompt)
        return response.content
