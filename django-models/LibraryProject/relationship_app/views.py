"""Views for the relationship_app."""
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .models import Book
from .models import Library


def list_books(request):
    """This view should render a simple text list of book titles and their authors."""
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request,'relationship_app/list_books.html', context)

def home(request):
    """A simple home view."""
    return render(request, 'relationship_app/home.html')

class libraryDetailView(DetailView):
    """Create a class-based view in relationship_app/views.py that displays details 
    for a specific library, listing all books available in that library."""
    model = Library #This the model that this view will use
    template_name = 'relationship_app/library_detail.html'

class user_registration(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'relationship_app/register.html'
    success_url = reverse_lazy('user_login')

class user_login(LoginView):
    template_name = 'relationship_app/login.html'
    redirect_authenticated_user = True

class user_logout(LogoutView):
    template_name = 'relationship_app/logout.html'
    http_method_names = ['get', 'post']
    # next_page = 'login'

   

