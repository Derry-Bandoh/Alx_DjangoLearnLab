from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from django.urls import reverse_lazy
from .serializers import BookSerializer
from .models import Book


class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    filterset_fields = ['title','author','publication_year']
    search_fields = ['title','author','publication_year']
    ordering_fields = ['title','author','publication_year']

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'

class BookCreateView(CreateView):
    model = Book
    template_name = 'book_form.html'
    fields = ['title', 'author', 'publication_year']
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthenticated]

    success_url = reverse_lazy('books')

class BookUpdateView(UpdateView):
    model = Book
    template_name = 'book_form.html'
    fields = ['title', 'author', 'publication_year']
    permission_classes = [IsAuthenticatedOrReadOnly,IsAuthenticated]

    success_url = reverse_lazy('books')


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'
    permission_classes = [IsAuthenticatedOrReadOnly,IsAuthenticated]

    success_url = reverse_lazy('books')


class BookListCreateAPIView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,IsAuthenticated]
    filterset_fields = ['title','author','publication_year']
    search_fields = ['title','author','publication_year']
    ordering_fields = ['title','author','publication_year']

class BookRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,IsAuthenticated]

