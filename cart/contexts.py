from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):
    "Function to manage the items in customer cart"
    user = request.user
    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get("cart", {})

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=product_id)
        if product.has_sale:
            total += quantity * product.sale_price
        else:
            total += quantity * product.price
        product_count += quantity
        cart_items.append(
            {
                "product_id": product_id,
                "quantity": quantity,
                "product": product,
                "product_count": product_count,
            }
        )

    if total < settings.FREE_SHIPPING_THRESHOLD:
        shipping = total * Decimal(settings.STANDARD_SHIPPING_PERCENTAGE / 100)
        free_shipping_delta = settings.FREE_SHIPPING_THRESHOLD - total
    else:
        shipping = 0
        free_shipping_delta = 0

    grand_total = shipping + total

    context = {
        "cart_items": cart_items,
        "total": total,
        "product_count": product_count,
        "shipping": shipping,
        "free_shipping_delta": free_shipping_delta,
        "free_shipping_threshold": settings.FREE_SHIPPING_THRESHOLD,
        "grand_total": grand_total,
        "user": user,
    }

    return context
