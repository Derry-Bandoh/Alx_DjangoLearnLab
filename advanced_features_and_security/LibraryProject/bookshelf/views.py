from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Book
from relationship_app.views import BookForm
from django.views.decorators.http import require_http_methods
from .forms import ExampleForm

# Create your views here.

#Get all books and check for 'can_view' permission
@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list_view(request):
    """View all books - requires 'can_view' permission"""
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

#Get the book instance and check for 'can_view' permission
@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def book_detail_view(request, pk):
    """View single book - requires 'can_view' permission"""
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})

#Get the book instance and check for 'can_add' permission
@login_required
@permission_required('bookshelf.can_add', raise_exception=True)
def book_create_view(request):
    """Create new book - requires 'can_add' permission"""
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            messages.success(request, f'Book "{book.title}" created successfully!')
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm()
    
    return render(request, 'books/book_form.html', {
        'form': form,
        'title': 'Add New Book'
    })


#Get the book instance and check for 'can_edit' permission

@login_required
def dashboard(request):
    """Dashboard view showing summary statistics"""
    total_books = Book.objects.count()
    return render(request, 'bookshelf/dashboard.html', {
        'total_books': total_books,
    })
@login_required
@permission_required('bookshelf.can_edit', raise_exception=True)
def book_update_view(request, pk):
    """Edit existing book - requires 'can_edit' permission"""
    book = get_object_or_404(Book, pk=pk)
    
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, f'Book "{book.title}" updated successfully!')
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    
    return render(request, 'books/book_form.html', {
        'form': form,
        'book': book,
        'title': 'Edit Book'
    })


#Get the book instance and check for 'can_delete' permission
@login_required
@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete_view(request, pk):
    """Delete book - requires 'can_delete' permission"""
    book = get_object_or_404(Book, pk=pk)
    
    if request.method == 'POST':
        title = book.title
        book.delete()
        messages.success(request, f'Book "{title}" deleted successfully!')
        return redirect('book_list')
    
    return render(request, 'books/book_confirm_delete.html', {'book': book})



@login_required  # Protect view with authentication
def search_books(request):
    form = SearchForm(request.GET or None)
    books = Book.objects.none()
    
    if form.is_valid():  # Form validation prevents malicious input
        query = form.cleaned_data['query']
        # Safe ORM query - parameterized and sanitized
        books = Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
        return render(request, 'bookshelf/book_list.html', {
        'books': books,
        'form': form
    })

# Safe detail view
def book_detail(request, book_id):
    
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'bookshelf/book_detail.html', {'book': book})

# Safe form handling
@login_required
@require_http_methods(["POST"])  # Only allow POST requests
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():  # Form validation prevents XSS and other attacks
            book = form.save(commit=False)
            book.created_by = request.user  # Set user safely
            book.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/book_form.html', {'form': form})