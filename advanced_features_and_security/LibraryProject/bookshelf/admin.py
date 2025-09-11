from django.contrib import admin
from .models import Book

# Custom admin configuration for the Book model
class BookAdmin(admin.ModelAdmin):
    # Display these fields in the admin list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add filters in the right sidebar
    list_filter = ('author', 'publication_year')
    
    # Add search functionality
    search_fields = ('title', 'author')
    
    # Optional: Add ordering
    ordering = ('title',)
    
    # Optional: Control how many items are shown per page
    list_per_page = 20

# Register the Book model with the custom admin configuration
admin.site.register(Book, BookAdmin)