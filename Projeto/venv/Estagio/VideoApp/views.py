from django.views.generic import DetailView, ListView
from .forms import Video_form
from django.shortcuts import render,redirect
from .models import (
    Post,
)

from django.http import HttpResponse


def home(request):
    return render(request, 'base.html')

def upload(request):
    all_video = Post.objects.all()
    if request.method == "POST":
        form = Video_form(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1> Uploaded successfully </h1>")
    else:
        form = Video_form()
    return render(request, 'index.html', {"form": form, "all": all_video})


def videos(request):
    all_video = Post.objects.all()
    if request.method == "POST":
        form = Video_form(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1> Uploaded successfully </h1>")
    else:
        form = Video_form()
    return render(request, 'post_list.html', {"form": form, "all": all_video})


def video(request):
    all_video = Post.objects.all()
    if request.method == "POST":
        form = Video_form(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1> Uploaded successfully </h1>")
    else:
        form = Video_form()
    return render(request, 'post_detail.html', {"form": form, "all": all_video})

