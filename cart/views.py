from django.shortcuts import render

from django.shortcuts import render


def view_cart(request):
    """A view that renders the cart content page"""

    return render(request, "cart/cart.html")
