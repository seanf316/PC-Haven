from django.contrib import admin
from .models import Wishlist


admin.site.register(Wishlist)


class WishlistAdmin(admin.ModelAdmin):
    search_fields = [
        "user",
    ]

    ordering = ("user",)
