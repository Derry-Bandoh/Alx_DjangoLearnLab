"""
Edit relationship_app/urls.py to include URL patterns that 
route to the newly created views. Make sure to link both the 
function-based and class-based views.
"""
from django.urls import path 
from .views import list_books, libraryDetailView
from .import views


urlpatterns = [
    path('views/', views.list_books),
    path('detail/', views.libraryDetailView.as_view()),
    ]