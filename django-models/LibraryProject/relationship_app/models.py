from django.db import models

class Author(models.Model):
    """Model representing a book author"""
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.name}"

class Book(models.Model):
    """Model representing a book with ForeignKey to Author"""
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.title} by {self.author.name}"

class Library(models.Model):
    """Model representing a library with ManyToMany relationship to Books"""
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, blank=True)
    
    def __str__(self):
        return f"{self.name}"

class Librarian(models.Model):
    """Model representing a librarian with OneToOne relationship to Library"""
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name} - {self.library.name}"