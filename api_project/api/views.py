# from django.shortcuts import render
from rest_framework.generics import ListAPIView
# from rest_framework.generics.ListAPIView import ListAPIView 
from .models import Book
from .serializers import BookSerializer 
from rest_framework.viewsets import ModelViewSet
# from rest_framework.viewsets.ModelViewSet
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated, IsAdminUser



class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(ModelViewSet, ObtainAuthToken):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


