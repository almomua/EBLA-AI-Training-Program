# Milestone 2 – RAG & Core Technologies

## Learning Objectives
- Understand Retrieval-Augmented Generation (RAG) architecture.
- Familiarize with a local LLM (Ollama) and an indexing library (LlamaIndex).

## Activities
- Study RAG architecture (retriever, generator, integration).
- Install and configure a local LLM (Ollama).
- Write initial scripts to interact with the chosen LLM and index a few documents.

## Deliverables
- [x] A discussion summary of RAG concepts.
- [x] A Python script demonstrating interaction with your chosen local LLM + a simple index build.

---

## Discussion Summary: RAG & Core Technologies

### 1. What is RAG?
RAG (Retrieval-Augmented Generation) combines **information retrieval** with **text generation** to produce accurate, context-aware responses using external documents.

| Component | Role |
|-----------|------|
| **Retriever** | Finds relevant document chunks |
| **Generator (LLM)** | Produces answers using retrieved context |
| **Embeddings** | Converts text to vectors for semantic search |

### 2. Local LLM (Ollama)
Ollama runs language models locally without API costs.

```bash
ollama pull gemma3:1b
ollama serve
```

### 3. LlamaIndex
LlamaIndex handles document loading, chunking, embedding, and retrieval.

```python
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, Settings
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

Settings.llm = Ollama(model="gemma3:1b")
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")

documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)
response = index.as_query_engine().query("Your question")
```

#### Document Chunking
When `VectorStoreIndex.from_documents()` is called, LlamaIndex automatically chunks documents into smaller pieces:

| Step | What Happens |
|------|-------------|
| **1. Load** | `SimpleDirectoryReader` loads PDFs/text files |
| **2. Chunk** | Documents are split into smaller chunks (~1024 tokens each) |
| **3. Embed** | Each chunk is converted to a vector using the embedding model |
| **4. Store** | Vectors are stored in the index for similarity search |

**Why chunking?** Large documents are split so that:
- Only relevant sections are retrieved (not entire documents)
- LLM context window limits are respected
- Search is more precise and efficient

**Note:** Chunking happens automatically inside `from_documents()` - no explicit chunking code is needed in the implementation.

---

## Project Structure (MVCS Pattern)

```
milestone-2/
├── app.py                    # Entry point
├── Models/
│   └── llm_model.py          # LLMConfig, LLMResponse dataclasses
├── Views/
│   └── chat_viewer.py        # CLI output formatting
├── Controllers/
│   └── rag_controller.py     # Coordinates services and view
├── Services/
│   ├── llm_service.py        # Direct Ollama interaction
│   └── index_service.py      # LlamaIndex RAG operations
├── data/                     # Documents to index
└── requirements.txt
```

## Files Overview

| File | Description |
|------|-------------|
| `app.py` | Runs the RAG demo |
| `Models/llm_model.py` | `LLMConfig` and `LLMResponse` data classes |
| `Views/chat_viewer.py` | Formats CLI output |
| `Controllers/rag_controller.py` | Routes requests to services |
| `Services/llm_service.py` | Wraps Ollama for direct chat |
| `Services/index_service.py` | Wraps LlamaIndex for RAG queries |

---

## Demo Output

```
✅ Successfully indexed 2 document(s).


🤖 Model: gemma3:1b
💡 Answer:
Please provide me with the documents! I need the text of the documents to be able to tell you the main topic. 😊 

To help me understand, please paste the documents here.


❓ Question: what is the second name after ahmed
💡 Answer: mostafa
```

**Note:** The `chat()` command talks directly to the LLM (no document context), while `query()` uses RAG to search the indexed documents and provide accurate answers.

---

## Resources Used

- [GeeksforGeeks - What is RAG?](https://www.geeksforgeeks.org/nlp/what-is-retrieval-augmented-generation-rag/)
- [LlamaIndex - Starter Tutorial (Local LLMs)](https://developers.llamaindex.ai/python/framework/getting_started/starter_example_local/)
- [Lightning AI - RAG using Llama 3](https://lightning.ai/lightning-ai/environments/rag-using-llama-3-by-meta-ai?view=public&section=featured)

---

## Notes

- Uses **Ollama** (gemma3:1b) as the local LLM.
- Uses **HuggingFace embeddings** (BAAI/bge-base-en-v1.5) for vectorization.
- Uses **LlamaIndex** for document indexing and retrieval.
- Follows the MVCS pattern and Google Python Style Guide.
