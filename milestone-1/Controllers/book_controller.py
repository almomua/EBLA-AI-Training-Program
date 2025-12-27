from typing import List
from Models.book_model import Book
from Views.book_view import BookView

class BookController:
    """Controls the flow of the book application."""

    def __init__(self):
        """Initializes the controller with view and books list."""
        self.view = BookView()
        self.books: List[Book] = []

    def run(self):
        """Starts the main application loop."""
        while True:
            choice = self.view.show_menu()

            if choice == '1':
                self._handle_add_book()
            elif choice == '2':
                self._handle_list_books()
            elif choice == '3':
                self.view.show_message("Goodbye!")
                break
            else:
                self.view.show_message("Invalid choice, please try again.")

    def _handle_add_book(self):
        """Handles the logic for adding a new book."""
        title, author = self.view.get_book_details()
        book = Book(title, author)
        self.books.append(book)
        self.view.show_message(f"Book '{title}' added successfully!")

    def _handle_list_books(self):
        """Handles the logic for listing all books."""
        book_strings = [str(book) for book in self.books]
        self.view.show_books(book_strings)


