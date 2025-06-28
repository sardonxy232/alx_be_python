# 0. Dive into Python Magic Methods
# mandatory
# Score: 0.0% (Checks completed: 0.0%)
# Objective: Master Python magic methods by implementing a Book class that incorporates constructors (__init__), destructors (__del__), and the representation methods (__str__ and __repr__).

# Task Description:
# Create a Python script named book_class.py. In this script, define a Book class that uses specific magic methods to enhance its functionality. This class will model a book with attributes for the title, author, and publication year.

# Requirements for Book Class in book_class.py:
# Attributes:

# title (str): The title of the book.
# author (str): The author of the book.
# year (int): The publication year of the book.
# Magic Methods:

# Constructor (__init__): Initializes a Book instance with title, author, and year.
# Destructor (__del__): Prints "Deleting (title of the book)" upon object deletion.
# String Representation (__str__): Returns a string in the format "(title) by (author), published in (year)".
# Official Representation (__repr__): Returns a string that would recreate the Book instance: f"Book('{self.title}', '{self.author}', {self.year})".
# Provided for Testing: main.py
# To test your Book class, use the following main.py script, which demonstrates creating a Book instance and utilizing the implemented magic methods:

# from book_class import Book

# def main():
#     # Creating an instance of Book
#     my_book = Book("1984", "George Orwell", 1949)

#     # Demonstrating the __str__ method
#     print(my_book)  # Expected to use __str__

#     # Demonstrating the __repr__ method
#     print(repr(my_book))  # Expected to use __repr__

#     # Deleting a book instance to trigger __del__
#     del my_book

# if __name__ == "__main__":
#     main()
# Expected Output:
# 1984 by George Orwell, published in 1949
# Book('1984', 'George Orwell', 1949)
# Deleting 1984
# Repo:

# GitHub repository: alx_be_python
# Directory: oop
# File: book_class.py

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        print(f"Deleting {self.title}")

    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
    
def main():
    # Creating an instance of Book
    my_book = Book("1984", "George Orwell", 1949)

    # Demonstrating the __str__ method
    print(my_book)  # Expected to use __str__

    # Demonstrating the __repr__ method
    print(repr(my_book))  # Expected to use __repr__

    # Deleting a book instance to trigger __del__
    del my_book

if __name__ == "__main__":
    main()
# If this script is run directly, it will execute the main function
# If imported, the main function will not run automatically
# This allows for testing the Book class without executing the main function
# when the module is imported elsewhere.
# This is a common practice in Python to allow for both direct execution and importation of modules.
# The main function serves as an entry point for testing the Book class.
# The Book class is now complete with the required magic methods.
# The main function demonstrates the functionality of the Book class.
# The Book class can be used in other scripts or modules as needed.
# The Book class is ready for use in the alx_be_python repository.
# The Book class can be extended or modified as needed for future requirements.