# Command used 
from bookshelf.models import Book

# Create a new Book instance
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()

# Alternative method using create()
# book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Output 

print(f"Book created with ID: {book.id}")
# Expected output: Book created with ID: 1

print(book.title)
# Expected output: 1984