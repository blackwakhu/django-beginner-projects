from django.shortcuts import render, get_object_or_404
from .models import *

def allAuthor(request):
  return render(request, "allAuthor.html", {"authors": Author.objects.all()})
