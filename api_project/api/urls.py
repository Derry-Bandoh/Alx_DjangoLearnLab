from django.urls import path
from rest_framework import routers
from .views import BookList

# router = routers.DefaultRouter()
# router.register(r'books', BookList)

urlpatterns = [
    # path('', include(router.urls)),
    path('books/', BookList.as_view(), name='book-list'),
]
