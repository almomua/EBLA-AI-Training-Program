from Services.retrieval_service import RetrievalService
from Schemas.api_schemas import SearchResponse, SearchResult


class RetrievalController:
    """Controller for search operations."""
    
    def __init__(self):
        self.service = RetrievalService()
    
    def search(self, query: str, top_k: int = 5) -> SearchResponse:
        """Handle search request."""
        results = self.service.search(query, top_k)
        
        search_results = []
        for r in results:
            search_results.append(SearchResult(
                content=r["content"],
                source=r["source"],
                score=r["score"]
            ))
        
        return SearchResponse(query=query, results=search_results)