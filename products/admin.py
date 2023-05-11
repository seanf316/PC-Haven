from django.contrib import admin
from .models import Product,CategoryGroup,SubCategory

admin.site.register(Product)
admin.site.register(CategoryGroup)
admin.site.register(SubCategory)
