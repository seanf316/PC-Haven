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

    if request.method == "POST":
        quantity = int(request.POST.get("quantity"))

        cart = request.session.get("cart", {})
        if product_id in cart:
            cart[product_id] += quantity
        else:
            cart[product_id] = quantity

        request.session["cart"] = cart

        return redirect(reverse("view_cart"))

    else:
        return HttpResponse("Invalid request")
