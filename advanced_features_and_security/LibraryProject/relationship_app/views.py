"""Views for the relationship_app."""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .models import Book
from .models import Library
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test 
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm





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

# class user_registration(CreateView):
#     model = User
#     form_class = UserCreationForm
#     template_name = 'relationship_app/register.html'
#     success_url = reverse_lazy('user_login')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

class user_login(LoginView):
    template_name = 'relationship_app/login.html'
    # redirect_authenticated_user = True

class user_logout(LogoutView):
    template_name = 'relationship_app/logout.html'
    #By default logoutview only accepts get requests
    #To allow post request, we need to specify the http_method_names attribute
    http_method_names = ['get', 'post']
    # next_page = 'login'

# Helper functions to check user roles
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# Role-based views
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author'] #, 'publication_year'

# Permission-secured views for book operations
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book added successfully!')
            return redirect('list_books')
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book updated successfully!')
            return redirect('list_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form, 'book': book})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Book deleted successfully!')
        return redirect('list_books')
    return render(request, 'relationship_app/delete_book.html', {'book': book})


   

