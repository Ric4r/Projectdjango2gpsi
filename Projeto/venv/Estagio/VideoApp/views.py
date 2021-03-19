from django.views.generic import DetailView, ListView

from .models import (
    Post,
    Videos
)


class PostListView(ListView):
    model = Post
    videos = Videos.objects.all()


class PostDetailView(DetailView):
    model = Post
    videos = Videos.objects.all()
