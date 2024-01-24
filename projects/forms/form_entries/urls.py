from django.urls import path
from . import views 

urlpatterns = [
  path("authors/", views.allAuthor, name="authors"),
  path("books/", views.allBook, name="allBook"),
]
