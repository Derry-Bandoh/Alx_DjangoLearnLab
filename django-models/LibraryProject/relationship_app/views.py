"""Views for the relationship_app."""
from django.shortcuts import render
from django.views.generic import ListView
from .models import Book


def book_list(request):
    """View to list all books."""
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request,'relationship_app/book_list.html', context)

class deatail_view(ListView):
    
    template_name = 'relationship_app/library_detail.html'
   

