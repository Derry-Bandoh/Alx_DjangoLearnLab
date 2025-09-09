"""
Edit relationship_app/urls.py to include URL patterns that 
route to the newly created views. Make sure to link both the 
function-based and class-based views.
"""
from django.urls import path 
from .import views
from .views import LibraryDetailView
from .views import list_books



urlpatterns = [
    path('views/', views.list_books, name= 'list_book'),
    path('detail/', views.libraryDetailView.as_view(), name= 'LibraryDetailView'),
    ]