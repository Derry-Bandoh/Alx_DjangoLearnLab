"""Views for the relationship_app."""
from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library


def book_list(request):
    """This view should render a simple text list of book titles and their authors."""
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request,'relationship_app/list_books.html', context)

class deatail_view(DetailView):
    """Create a class-based view in relationship_app/views.py that displays details 
    for a specific library, listing all books available in that library."""
    model = Library #This the model that this view will use
    template_name = 'relationship_app/library_detail.html'
   

