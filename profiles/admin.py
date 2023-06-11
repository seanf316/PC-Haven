from django.contrib import admin
from .models import Wishlist


class WishlistAdmin(admin.ModelAdmin):
    """
    Admin registration and configuration
    for the Wishlist model
    """
    search_fields = [
        "user",
    ]

    ordering = ("user",)


admin.site.register(Wishlist, WishlistAdmin)
