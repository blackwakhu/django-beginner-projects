from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("authors/", views.allAuthor, name="allAuthor"),
    path("books/", views.allBook, name="allBook"),
    path("author/<int:author_id>", views.author, name="author"),
    path("book/<int:book_id>", views.book, name="book"),
]
