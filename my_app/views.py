from django.shortcuts import render,HttpResponse
from .models import Book,Author
from .serializer import AuthorSerializer,BookSerializer
from rest_framework import generics

def index(request):
    return HttpResponse("Hello")

# Author Api creation section 
class AuthorListView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

# Author Api creation section end

# Boook Api creation section
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Boook Api creation section end