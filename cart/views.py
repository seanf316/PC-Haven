from django.shortcuts import (
    render,
    redirect,
    reverse,
    HttpResponse,
    get_object_or_404,
)
from django.contrib import messages
from products.models import Product


def view_cart(request):
    """A view that renders the cart content page"""

    return render(request, "cart/cart.html")


def add_to_cart(request, product_id):
    """Add a product and its quantity to the cart"""

    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")
    cart = request.session.get("cart", {})

    if product_id in list(cart.keys()):
        cart[product_id] += quantity
    else:
        cart[product_id] = quantity

    request.session["cart"] = cart

    return render(request, "cart/cart.html")
