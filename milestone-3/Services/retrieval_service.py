from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


class RetrievalService:
    """Service for searching indexed documents in ChromaDB."""
    
    def __init__(self, embed_model: str = "BAAI/bge-base-en-v1.5"):
        self.embeddings = HuggingFaceEmbeddings(model_name=embed_model)
        self.persist_dir = "milestone-3/storage/chroma_db"
        self.vectorstore = None
    
    def load_store(self):
        """Load ChromaDB from disk."""
        self.vectorstore = Chroma(
            persist_directory=self.persist_dir,
            embedding_function=self.embeddings
        )
    
    def search(self, query: str, top_k: int = 5) -> list[dict]:
        """Search for relevant documents.
        
        Args:
            query: Search query text
            top_k: Number of results to return
        
        Returns:
            List of results with content, source, score
        """
        if self.vectorstore is None:
            self.load_store()
        
        results = self.vectorstore.similarity_search_with_score(query, k=top_k)
        
        output = []
        for doc, score in results:
            output.append({
                "content": doc.page_content,
                "source": doc.metadata.get("source", "unknown"),
                "score": float(score)
            })
        return output

