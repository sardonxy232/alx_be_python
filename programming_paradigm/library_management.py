class Book:
    """Represents a book in the library."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Marks the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True

    def return_book(self):
        """Marks the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False

    def is_available(self):
        """Returns True if the book is not checked out."""
        return not self._is_checked_out


class Library:
    """Manages a collection of books."""

    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Adds a Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Checks out a book by title if it is available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return
        print(f"Book '{title}' is not available or does not exist.")

    def return_book(self, title):
        """Returns a book by title if it is found in the library."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return
        print(f"Book '{title}' is not checked out or does not exist.")

    def list_available_books(self):
        """Prints all books that are currently available."""
        available = [book for book in self._books if book.is_available()]
        if not available:
            print("No available books.")
        else:
            for book in available:
                print(f"{book.title} by {book.author}")
