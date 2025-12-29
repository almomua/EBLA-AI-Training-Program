from fastapi import APIRouter, UploadFile, File, Form
from typing import Optional
from Controllers.index_controller import IndexController
from Schemas.api_schemas import IndexResponse

router = APIRouter()



@router.post("/index", response_model=IndexResponse)
async def index_document(
    file: Optional[UploadFile] = File(None),
    content: Optional[str] = Form(None),
    source: str = Form("document.txt")
):
    """Index a document (file upload OR raw text).
    
    - Send a file: use 'file' field
    - Send raw text: use 'content' field (source defaults to 'document.txt')
    """
    if file:
        file_bytes = await file.read()
        return IndexController().index_file(file_bytes, file.filename)
    
    if content:
        return IndexController().index_text(content, source)
    
    return IndexResponse(
        success=False,
        message="Provide either a file OR content",
        chunks_indexed=0
    )

