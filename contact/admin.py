from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    """
    Class to display Contact queries in admin view
    """
    list_display = (
        "date_received",
        "contact_reason",
        "name",
        "email",
        "pending_reply",
        "marked_as_done",
    )

    list_filter = ("pending_reply", "marked_as_done", "date_received")

    ordering = ("-date_received",)


admin.site.register(Contact, ContactAdmin)
