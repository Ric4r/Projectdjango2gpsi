from django.contrib import admin
from .models import Post
from embed_video.admin import AdminVideoMixin
from .models import Videos


class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass


admin.site.register(Videos, MyModelAdmin)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "author", "created", "updated")
    prepopulated_fields = {"slug": ("title",)}
