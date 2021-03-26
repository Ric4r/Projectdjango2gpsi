from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "VideoApp"



urlpatterns = [
    path('Upload/', views.upload),
    path('videos/', views.videos),
    path('videos/video/', views.video),
    path('', views.home),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)