from rest_framework import serializers
from .models import Book, Author
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_date']
    
    def validate(self, attrs):
        if attrs['published_date'] > date.today():
            raise serializers.ValidationError("Published date cannot be in the future.")
        return attrs
        

class AuthorSerializer(serializers.ModelSerializer):
    author = BookSerializer(read_only=True, many=True)
    class Meta:
        model = Author
        fields = ['id', 'name', 'author']