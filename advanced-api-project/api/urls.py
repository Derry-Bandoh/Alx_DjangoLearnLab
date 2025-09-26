from django.urls import path
from .views import (
    BookListCreateAPIView,
    BookRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path('books/', BookListCreateAPIView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view(), name='book-detail'),
    path('books/<int:pk>/create', BookListCreateAPIView.as_view(), name='book-create'),
    path('books/<int:pk>/update', BookRetrieveUpdateDestroyAPIView.as_view(), name='book-update'),
    path('books/<int:pk>/delete', BookRetrieveUpdateDestroyAPIView.as_view(), name='book-delete'),
]