from django.views.generic import DetailView, ListView
from .forms import Video_form
from django.shortcuts import render,HttpResponse,redirect
from .models import (
    Post,
    Videos
)


def index(request):
    all_video=Post.objects.all()
    if request.method == "POST":
        form=Video_form(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1> Uploaded successfully </h1>")
    else:
        form=Video_form()
    return render(request,'index.html',{"form":form,"all":all_video})


class PostListView(ListView):
    model = Post
    videos = Videos.objects.all()



class PostDetailView(DetailView):
    model = Post
    videos = Videos.objects.all()


