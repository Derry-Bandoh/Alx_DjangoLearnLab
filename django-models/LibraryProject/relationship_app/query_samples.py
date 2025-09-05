import os
import django



# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from .models import Author, Book, Library, Librarian


def query_books_by_author():
    """Query all books by a specific author (ForeignKey relationship)"""
    try:
        # Get a specific author 
        author_name = "J.K. Rowling"
        author = Author.objects.get(name=author_name)
        
        # Query all books by this author
        books = Book.objects.filter(author=author)
        
        print(f"\n--- Books by {author_name} ---")
        for book in books:
            print(f"- {book.title}")
            
            
    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found")

def query_books_in_library():
    """List all books in a library (ManyToMany relationship)"""
    try:
        # Get a specific library
        library_name = "Central Library"
        library = Library.objects.get(name=library_name)
        
        # Query all books in this library
        books = library.books.all()
        
        print(f"\n--- Books in {library_name} ---")
        for book in books:
            print(f"- {book.title} by {book.author.name}")
            
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found")

def query_librarian_for_library():
    """Retrieve the librarian for a library (OneToOne relationship)"""
    try:
        # Get a specific library
        library_name = "Central Library"
        library = Library.objects.get(name=library_name)
        
        # Get the librarian for this library
        librarian = library.librarian
        
        print(f"\n--- Librarian for {library_name} ---")
        print(f"Librarian: {librarian.name}")

        
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found")
    except Librarian.DoesNotExist:
        print(f"No librarian found for {library_name}")
