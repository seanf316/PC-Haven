from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Product, CategoryGroup, SubCategory


class ProductAdmin(SummernoteModelAdmin):
    """
    Admin registration and configuration for the Product model
    Staff can see all products and filter them as
    desired
    """

    list_display = (
        "name",
        "category",
        "sub_category",
        "sku",
        "price",
        "in_stock",
    )

    search_fields = (
        "name",
        "description",
        "information",
        "sku",
        "category__name",
        "sub_category__name",
    )

    list_filter = (
        "category",
        "sub_category",
        "in_stock",
    )

    summernote_fields = ("description", "information")


class CategoryGroupAdmin(admin.ModelAdmin):
    """
    Admin registration and configuration
    for the Categories Group model
    """

    list_display = (
        "friendly_name",
        "name",
    )


class SubCategoryAdmin(admin.ModelAdmin):
    """
    Admin registration and configuration
    for the Sub Categories model
    """

    list_display = (
        "friendly_name",
        "name",
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(CategoryGroup, CategoryGroupAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
