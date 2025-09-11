# COMMNAND USED 
from bookshelf.models import Book

# Retrieve the book to update
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Verify the update
print(f"Updated title: {book.title}")

# OUTPUT 
Updated title: Nineteen Eighty-Four