class Book:
    total_books = 0  # Class variable to track the total number of books

    def __init__(self, title, author):
        # Instance variables
        self.title = title
        self.author = author
        # Increment the total book count when a new book is created
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        # Class method to increment the total book count
        cls.total_books += 1

    @classmethod
    def get_total_books(cls):
        # Class method to get the current count of books
        return cls.total_books

# Example usage
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("1984", "George Orwell")
book3 = Book("To Kill a Mockingbird", "Harper Lee")

# Display the total number of books
print(f"Total number of books: {Book.get_total_books()}")
