from django.contrib import admin
from .models import Post


class PostAdming(admin.ModelAdmin):
    list_display = ["author", "title", "slug", "published_status"]

    class Meta:
        model = Post


admin.site.register(Post, PostAdming)
