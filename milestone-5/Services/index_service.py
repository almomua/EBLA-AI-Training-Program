from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from Utils.file_loader import load_file
from Models.document_model import DocumentModel


class IndexService:
    """Service for indexing documents into ChromaDB."""
    
    def __init__(self, embed_model: str = "BAAI/bge-base-en-v1.5"):
        self.embeddings = HuggingFaceEmbeddings(model_name=embed_model)
        self.splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        self.persist_dir = "milestone-5/storage/chroma_db"
    
    def index_text(self, content: str, source: str) -> int:
        """Index raw text content."""
        doc = DocumentModel(page_content=content, metadata={"source": source})
        documents = [doc.to_langchain_document()]
        return self._process_and_store(documents)
    
    def index_file(self, file_bytes: bytes, filename: str) -> int:
        """Index uploaded file."""
        documents = load_file(file_bytes, filename)  # Use util
        return self._process_and_store(documents)
    
    def _process_and_store(self, documents: list[Document]) -> int:
        """Split documents and store in ChromaDB."""
        chunks = self.splitter.split_documents(documents)
        
        Chroma.from_documents(
            documents=chunks,
            embedding=self.embeddings,
            persist_directory=self.persist_dir
        )
        
        return len(chunks)