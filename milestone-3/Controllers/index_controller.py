from Services.index_service import IndexService
from Schemas.api_schemas import IndexResponse


class IndexController:
    """Controller for indexing operations."""
    
    def __init__(self):
        self.service = IndexService()
    
    def index_text(self, content: str, source: str) -> IndexResponse:
        """Handle raw text indexing."""
        chunks = self.service.index_text(content, source)
        return IndexResponse(
            success=True,
            message=f"Indexed {source}",
            chunks_indexed=chunks
        )
    
    def index_file(self, file_bytes: bytes, filename: str) -> IndexResponse:
        """Handle file upload indexing."""
        chunks = self.service.index_file(file_bytes, filename)
        return IndexResponse(
            success=True,
            message=f"Indexed {filename}",
            chunks_indexed=chunks
        )