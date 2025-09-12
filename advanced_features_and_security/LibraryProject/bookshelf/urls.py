from django.urls import path
from . import views

urlpatterns = [
    path('AvailableBooks/', views.book_list_view, name='book_list'),
    path('BookDetail/<int:pk>/', views.book_detail_view, name='book_detail'),
    path('AddBook/', views.book_create_view, name='book_create'),
    path('EditBook/<int:pk>/', views.book_update_view, name='book_update'),
    path('DeleteBook/<int:pk>/', views.book_delete_view, name='book_delete'),
    path('Home/', views.dashboard, name='book_dashboard'),
]