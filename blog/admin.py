from django.contrib import admin
from .models import Blog
from django_summernote.admin import SummernoteModelAdmin


class BlogAdmin(SummernoteModelAdmin):
    list_filter = ("created_on",)
    list_display = (
        "title",
        "author",
        "created_on",
    )
    search_fields = ["title", "content"]
    summernote_fields = "content"


admin.site.register(Blog, BlogAdmin)
