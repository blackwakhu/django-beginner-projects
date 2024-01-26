from django import forms
from .models import *


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"


class BookForm(forms.Form):
    isdn = forms.CharField(max_length=10)
    title = forms.CharField(max_length=100)
    year = forms.IntegerField()
    genre = forms.CharField(max_length=25)
    edition = forms.IntegerField()
