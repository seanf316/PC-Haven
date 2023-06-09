from django.contrib import admin
from .models import Wishlist


class WishlistAdmin(admin.ModelAdmin):
    search_fields = [
        "user",
    ]

    ordering = ("user",)


admin.site.register(Wishlist, WishlistAdmin)
