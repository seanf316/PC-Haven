from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ("lineitem_total",)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = (
        "order_number",
        "order_date",
        "delivery_cost",
        "order_total",
        "grand_total",
    )

    fields = (
        "order_number",
        "order_date",
        "full_name",
        "email",
        "phone_number",
        "street_address1",
        "street_address2",
        "town_or_city",
        "county",
        "postcode",
        "country",
        "delivery_cost",
        "order_total",
        "grand_total",
    )

    list_display = (
        "order_number",
        "order_date",
        "full_name",
        "order_total",
        "delivery_cost",
        "grand_total",
    )

    ordering = ("-order_date",)


admin.site.register(Order, OrderAdmin)
