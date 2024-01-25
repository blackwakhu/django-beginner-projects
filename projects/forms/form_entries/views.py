from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Author, Book

# Create your views here.

def index(request):
  return HttpResponse("we are the champions")

def allAuthor(request):
  return render(request, "allAuthor.html", {"authors": Author.objects.all()})

def allBook(request):
  return render(request, "allBook.html", {"books": Book.objects.all()})

def author(request, author_id):
  return render(request, "author.html", {"data": get_object_or_404(Author, pk=author_id)})


def book(request, book_id):
  return render(request, "book.html", {"data": get_object_or_404(Book, pk=book_id)})

