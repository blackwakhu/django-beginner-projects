from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("authors/", views.allAuthor, name="allAuthor"),
    path("books/", views.allBook, name="allBook"),
    path("author/<int:author_id>", views.author, name="author"),
    path("book/<int:book_id>", views.book, name="book"),
    path("author/create", views.createAuthor, name="createAuthor"),
    path("book/create/<int:author_id>", views.createBook, name="createBook"),
    path("book/delete/<int:book_id>", views.deleteBook, name="deleteBook"),
    path("author/delete/<int:author_id>", views.deleteAuthor, name="deleteAuthor"),
    path("author/update/<str:param>/<int:author_id>", views.updateAuthor, name="updateAuthor"),
    path("book/update/<str:param>/<int:book_id>", views.updateBook, name="updateBook"),
]
