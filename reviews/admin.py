from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Review


@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    """
    Admin registration and configuration for the Review model
    Staff can see all reviews and filter them as
    desired
    """

    list_display = (
        "user",
        "product",
        "rating",
    )

    search_fields = (
        "user",
        "product",
    )

    list_filter = (
        "user",
        "product",
        "rating",
    )

    summer_fields = "review"
