1. CREATE Operation
Command:
# Create a new Book instance
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()

# Verify creation
print(f"Book created with ID: {book.id}")
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Year: {book.publication_year}")

Output: 
Book created with ID: 1
Title: 1984
Author: George Orwell
Publication Year: 1949



2. RETRIEVE Operation
Command:
# Retrieve the book we created
book = Book.objects.get(title="1984")

# Display all attributes
print(f"ID: {book.id}")
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Year: {book.publication_year}")

# Show all books
all_books = Book.objects.all()
print(f"All books: {all_books}")

Output: 
ID: 1
Title: 1984
Author: George Orwell
Publication Year: 1949
All books: <QuerySet [<Book: 1984>]>



3. UPDATE Operation
Command:
# Retrieve the book to update
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Verify the update
print(f"Updated title: {book.title}")

# Confirm the change persisted in database
updated_book = Book.objects.get(id=book.id)
print(f"Title from database: {updated_book.title}")

Output: 
Updated title: Nineteen Eighty-Four
Title from database: Nineteen Eighty-Four



4. DELETE Operation
Command:
# Retrieve the book to delete
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
delete_result = book.delete()
print(f"Delete result: {delete_result}")

# Confirm deletion
all_books = Book.objects.all()
print(f"All books after deletion: {all_books}")
print(f"Total books in database: {Book.objects.count()}")

# Try to retrieve the deleted book
try:
    deleted_book = Book.objects.get(title="Nineteen Eighty-Four")
except Book.DoesNotExist:
    print("Confirmed: Book successfully deleted - not found in database")

Output: 
Delete result: (1, {'bookshelf.Book': 1})
All books after deletion: <QuerySet []>
Total books in database: 0
Confirmed: Book successfully deleted - not found in database