"""
Edit relationship_app/urls.py to include URL patterns that 
route to the newly created views. Make sure to link both the 
function-based and class-based views.
"""
from django.urls import path 
from .import views
# from django.contrib.auth import views as auth_views
# from .views import LibraryDetailView
# from .views import list_books



urlpatterns = [
    path('views/', views.list_books, name= 'list_book'),
    path('detail/', views.libraryDetailView.as_view(), name= 'LibraryDetailView'),
    path('register/', views.user_registration.as_view(), name= 'register'),
    path('login/',views.user_login.as_view(), name= 'login'),
    path('logout/',views.user_logout.as_view(), name = 'logout'),
    path('', views.home, name='home'),
    ]