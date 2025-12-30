from fastapi import APIRouter
from Controllers.ask_controller import AskController
from Schemas.api_schemas import AskRequest, AskResponse

router = APIRouter()


@router.post("/ask", response_model=AskResponse)
def ask_question(request: AskRequest):
    """Ask a question and get an LLM-generated answer using RAG."""
    return AskController(model_name="gemma3:1b").ask(request.query, request.top_k)
