from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import Author, Book
from .forms import AuthorForm, BookForm

# Create your views here.

def index(request):
  return HttpResponse("we are the champions")

def allAuthor(request):
  return render(request, "allAuthor.html", {"authors": Author.objects.all()})

def allBook(request):
  return render(request, "allBook.html", {"books": Book.objects.all()})

def author(request, author_id):
  return render(request, "author.html", {"data": get_object_or_404(Author, pk=author_id), "books": Book.objects.filter(author_id=author_id)})

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
      author.book_set.create(isdn=form.cleaned_data['isdn'], title=form.cleaned_data['title'], year=form.cleaned_data['year'], genre=form.cleaned_data['genre'], edition=form.cleaned_data['edition'])
      return redirect(f"/form/author/{author_id}")
  return render(request, "createBook.html", {"form": form})
  
