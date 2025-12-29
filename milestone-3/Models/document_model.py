from dataclasses import dataclass, field


@dataclass
class DocumentModel:
    """Standard document model matching LangChain's structure."""
    page_content: str
    metadata: dict = field(default_factory=dict)

    def to_langchain_document(self):
        """Convert to LangChain Document object."""
        from langchain_core.documents import Document
        return Document(page_content=self.page_content, metadata=self.metadata)
