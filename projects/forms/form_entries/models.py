from django.db import models

# Create your models here.

class Author(models.Model):
  fname =  models.CharField(max_length=25)
  lname = models.CharField(max_length=25)
  email = models.EmailField(max_length=50)
  
  def __str__(self):
    return f"{fname} {lname}"

class Book(models.Model):
  isdn = models.CharField(max_length=10) 
  title = models.CharField(max_length=25)
  year = models.IntegerField(default=2000) 
  genre = models.CharField(max_length=25)
  edition = models.IntegerField(default=1)
  author = models.ForeignKey(Author, on_delete=models.CASCADE)

  def __str__(self):
    return self.title

