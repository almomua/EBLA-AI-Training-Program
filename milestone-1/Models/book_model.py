"""Book class that represents a single book entity with a title and author."""


class Book:
    """Represents a single book entity with a title and author."""

    def __init__(self, title: str, author: str, available: bool = True):
        """Initializes a Book instance.

        Args:
            title: The title of the book.
            author: The author of the book.
            available: Whether the book is available.
        """
        self.title: str = title
        self.author: str = author
        self.available: bool = available

    def __str__(self) -> str:
        """Returns a string representation of the book."""
        return f"'{self.title}' by {self.author} is {'available' if self.available else 'not available'}"

    def to_dict(self) -> dict:
        """Returns the book as a dictionary.

        Returns:
            A dictionary containing the book's attributes.
        """
        return {
            "title": self.title,
            "author": self.author,
            "available": self.available
        }
