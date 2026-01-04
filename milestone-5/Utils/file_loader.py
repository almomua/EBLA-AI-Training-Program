from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_core.documents import Document
import tempfile
import os


def load_file(file_bytes: bytes, filename: str) -> list[Document]:
    """Load file and return LangChain Documents.
    
    Args:
        file_bytes: Raw file content
        filename: Original filename (to detect type)
    
    Returns:
        List of LangChain Document objects
    """
    suffix = os.path.splitext(filename)[1]
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(file_bytes)
        tmp_path = tmp.name
    
    if filename.endswith(".pdf"):
        loader = PyPDFLoader(tmp_path)
    else:
        loader = TextLoader(tmp_path)
    
    documents = loader.load()
    os.unlink(tmp_path)  # Clean up
    
    return documents