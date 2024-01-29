from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import Author, Book
from .forms import *

# Create your views here.

def index(request):
  return HttpResponse("we are the champions")

def allAuthor(request):
  return render(request, "allAuthor.html", {"authors": Author.objects.all()})

def allBook(request):
  return render(request, "allBook.html", {"books": Book.objects.all()})

def author(request, author_id):
  data = {
    "data": get_object_or_404(Author, pk=author_id),
    "books": Book.objects.filter(author_id=author_id)
  }
  return render(request, "author.html", data)

def book(request, book_id):
  return render(request, "book.html", {"data": get_object_or_404(Book, pk=book_id)})

def createAuthor(request):
  form = AuthorForm()
  if request.method == "POST":
    form = AuthorForm(request.POST)
    if form.is_valid():
      form.save()
    return redirect("/form/authors")
  return render(request, "createAuthor.html", {"form": form})


def createBook(request, author_id):
  form = BookForm()
  if request.method == "POST":
    form = BookForm(request.POST)
    if form.is_valid():
      # print(form.cleaned_data['isdn'])
      author = Author.objects.get(pk=author_id)
      author.book_set.create(
        isdn=form.cleaned_data['isdn'], 
        title=form.cleaned_data['title'], 
        year=form.cleaned_data['year'], 
        genre=form.cleaned_data['genre'], 
        edition=form.cleaned_data['edition'])
      return redirect(f"/form/author/{author_id}")
  return render(request, "createBook.html", {"form": form})

def deleteBook(request, book_id):
  book = get_object_or_404(Book, pk=book_id)
  book.delete()
  return redirect("/form/books")

def deleteAuthor(request, author_id):
  author = get_object_or_404(Author, pk=author_id)
  author.delete()
  return redirect("/form/authors")

def updateAuthor(request, param, author_id):
  author = get_object_or_404(Author, pk=author_id)
  if param == "fname":
    author.fname = request.POST.get('data')
  elif param == "lname":
    author.lname = request.POST.get('data')
  elif param == "email":
    author.email = request.POST.get('data')
  author.save()
  return redirect(f"/form/author/{author_id}")

def updateBook(request, param, book_id):
  book = get_object_or_404(Book, pk=book_id)
  if param == "isdn":
    book.isdn = request.POST.get('data')
  elif param == "title":
    book.title = request.POST.get('data')
  elif param == "year":
    book.year = request.POST.get('data')
  elif param == "year":
    book.genre = request.POST.get('data')
  elif param == "year":
    book.edition = request.POST.get('data')
  book.save()
  return redirect(f"/form/book/{book_id}")
