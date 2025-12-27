from typing import List

class BookView:
    """Handles the user interface interactions."""

    def show_menu(self) -> str:
        """Displays the menu options and returns user choice."""
        print("\n--- Book Manager ---")
        print("1. Add a Book")
        print("2. List all Books")
        print("3. Exit")
        return input("Select an option: ")

    def get_book_details(self) -> tuple[str, str]:
        """Prompts user for book title and author."""
        print("\n[Add New Book]")
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        return title, author

    def show_books(self, books_summary: List[str]):
        """Displays a list of books from string summaries.
        
        Args:
            books_summary: A list of formatted strings representing books.
        """
        print("\n[Book List]")
        if not books_summary:
            print("No books available.")
        else:
            for summary in books_summary:
                print(f"- {summary}")

    def show_message(self, message: str):
        """Displays a system message."""
        print(f"Server: {message}")