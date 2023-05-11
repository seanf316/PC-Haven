from django.contrib import admin
from .models import Product,CategoryGroup,SubCategory

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Admin registration and configuration for the Product model
    Staff can see all products and filter them as
    desired
    """
    
    list_display = (
        'category',
        'sub_category',
        'sku',
        'name',
        'price',
        'in_stock',
        'image')
    
    search_fields = (
        'name',
        'description',
        'information',
        'sku',
        'category__name',
        'sub_category__name',
    )

    list_filter = (
        'category',
        'sub_category',
        'in_stock',
    )

@admin.register(CategoryGroup)
class CategoryGroupAdmin(admin.ModelAdmin):
    """
    Admin registration and configuration
    for the Categories Group model
    """
    list_display = (
        'friendly_name',
        'name',
    )

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    """
    Admin registration and configuration
    for the Sub Categories model
    """
    list_display = (
        'friendly_name',
        'name',
    )

