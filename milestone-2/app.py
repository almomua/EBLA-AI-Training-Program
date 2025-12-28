from Controllers.rag_controller import RAGController
if __name__ == "__main__":
    rag_controller = RAGController(model_name="gemma3:1b", embed_model_name="BAAI/bge-base-en-v1.5", data_dir="milestone-2\data")
    rag_controller.index_documents()
    rag_controller.chat("What is the main topic of the documents?")
    rag_controller.query("what is the second name after ahmed")
