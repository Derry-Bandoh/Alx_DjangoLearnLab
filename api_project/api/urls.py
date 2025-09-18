from django.urls import path, include 
from rest_framework import routers
from .views import BookList, BookViewSet

router = routers.DefaultRouter()
router.register(r'books_all', BookViewSet , basename='books_all')

urlpatterns = [
    path('', include(router.urls)),
    path('books/', BookList.as_view(), name='book-list'),
]
