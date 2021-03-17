from django.urls import path

from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "VideoApp"

urlpatterns = [
    path("", views.PostListView.as_view(), name="list"),
    path("<slug:slug>/", views.PostDetailView.as_view(), name="detail"),
]

urlpatterns += staticfiles_urlpatterns()