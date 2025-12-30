from langchain_ollama import ChatOllama


class LLMService:
    """Service for interacting with Ollama LLM."""
    
    def __init__(self, model_name: str = "gemma3:1b"):
        self.llm = ChatOllama(model=model_name)
    
    def generate(self, query: str, context: list[str]) -> str:
        """Generate a response using retrieved context.
        
        Args:
            query: User's question
            context: List of relevant document chunks
        
        Returns:
            LLM generated answer
        """
        context_text = "\n\n".join(context)
        
        prompt = f"""Use the following context to answer the question. 
If the answer is not in the context, say "I don't have enough information to answer this question."

Context:
{context_text}

Question: {query}

Answer:"""
        
        response = self.llm.invoke(prompt)
        return response.content  # Extract string from AIMessage