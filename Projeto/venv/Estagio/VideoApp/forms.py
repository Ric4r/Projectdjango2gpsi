from .models import Post
from django import forms

class Video_form(forms.ModelForm):
    class Meta:
        model=Post
        fields=("title","slug","author","body","thumb"
                ,"videos")