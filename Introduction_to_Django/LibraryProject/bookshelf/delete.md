# COMMAND USED 
from bookshelf.models import Book

# Retrieve the book to delete
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# OUTPUT 
# Expected output after delete():
(1, {'bookshelf.Book': 1})
# This indicates 1 object was deleted from the bookshelf.Book model