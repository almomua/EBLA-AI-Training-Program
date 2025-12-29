from fastapi import APIRouter
from Controllers.retrieval_controller import RetrievalController
from Schemas.api_schemas import SearchRequest, SearchResponse

router = APIRouter()


@router.post("/search", response_model=SearchResponse)
def search_documents(request: SearchRequest):
    """Search indexed documents."""
    return RetrievalController().search(request.query, request.top_k)

