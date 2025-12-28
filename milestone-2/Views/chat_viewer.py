# Views/cli_view.py
from Models.llm_model import LLMResponse


class ChatViewer:
    """Formats and displays output for the command line."""
    
    def display_welcome(self) -> None:
        """Display welcome message."""
        print("\n" + "=" * 50)
        print("  Milestone 2: RAG Demo - LLM + Indexing")
        print("=" * 50)
        print("Commands: chat, index, query, quit\n")
    
    def display_llm_response(self, response: LLMResponse) -> None:
        """Display LLM response.
        
        Args:
            response: The LLM response to display.
        """
        print(f"\n🤖 Model: {response.model}")
        print(f"💡 Answer:\n{response.answer}\n")
    
    def display_index_success(self, doc_count: int) -> None:
        """Display indexing success message.
        
        Args:
            doc_count: Number of documents indexed.
        """
        print(f"\n✅ Successfully indexed {doc_count} document(s).\n")
    
    def display_query_result(self, question: str, answer: str) -> None:
        """Display query result.
        
        Args:
            question: The user's question.
            answer: The answer from the index.
        """
        print(f"\n❓ Question: {question}")
        print(f"💡 Answer: {answer}\n")
    
    def display_error(self, message: str) -> None:
        """Display error message.
        
        Args:
            message: The error message.
        """
        print(f"\n❌ Error: {message}\n")
    
    def prompt_input(self, prompt: str) -> str:
        """Get input from user.
        
        Args:
            prompt: The prompt to display.
            
        Returns:
            User's input string.
        """
        return input(prompt).strip()