
from django.contrib import admin
from .models import  Post
from embed_video.admin import AdminVideoMixin

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title","slug","author","created","updated","videos")
    prepopulated_fields ={"slug":("title",)}
    Post = ("title","slug","author","body","created","updated","thumb","video")