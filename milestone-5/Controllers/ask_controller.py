from Services.retrieval_service import RetrievalService
from Services.llm_service import LLMService
from Schemas.api_schemas import AskResponse


class AskController:
    """Controller for RAG question-answering."""
    
    def __init__(self , model_name: str = "gemma3:1b" , embed_model: str = "BAAI/bge-base-en-v1.5"):
        self.retrieval_service = RetrievalService(embed_model=embed_model)
        self.llm_service = LLMService(model_name=model_name)
    
    def ask(self, query: str, top_k: int = 3) -> AskResponse:
        """Retrieve relevant docs and generate answer."""
        
        # 1. Retrieve relevant chunks from ChromaDB
        results = self.retrieval_service.search(query, top_k)
        
        # 2. Extract content and sources
        context = [r["content"] for r in results]
        sources = [r["source"] for r in results]
        
        # 3. Generate answer using LLM with context
        answer = self.llm_service.generate(query=query, context=context)
        
        return AskResponse(
            query=query,
            answer=answer,
            sources=list(set(sources))  
            
        )