from django.test import TestCase
from rest_framework.test  import APITestCase
from .models import Book
from rest_framework import status, response.data 

class BookTestCase(TestCase):

class BookViewTests(TestCase,APITestCase):
    def test_book_list_status_code(self):
        # Simulate a GET request to the book-list URL
        response = self.client.get('/api/books/') 
        response = self.client.login('/api/login/')
        
        # Assertions
        self.assertEqual(response.status_code, 200) # Check for a successful response
        self.assertContains(response, 'Test Title') # Check if the content is in the response


class BookModelTests(TestCase, APITestCase):
    def setUp(self):
        # Create an object available to all test methods
        self.book = Book.objects.create(title='Test Title', author='Test Author')

    def test_book_title_max_length(self):
        # Your actual test logic
        max_length = self.book._meta.get_field('title').max_length
        self.assertEqual(max_length, 100) # Check if the max_length is 100
    
    def test_book_str_method(self):
        # Check if the __str__ method returns the expected string
        self.assertEqual(str(self.book), 'Test Title')
