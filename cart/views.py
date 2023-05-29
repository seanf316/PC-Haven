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
        product = get_object_or_404(Product, id=product_id)
        quantity = int(request.POST.get("quantity"))

        cart = request.session.get("cart", {})
        if product_id in cart:
            cart[product_id] += quantity
            messages.success(
                request,
                f"Updated {product.name} quantity to {cart[product_id]}",
            )
        else:
            cart[product_id] = quantity
            messages.success(request, f"Added {product.name} to cart.")
        request.session["cart"] = cart

        return redirect(reverse("products"))

    else:
        return HttpResponse("Invalid request")


def edit_cart(request, product_id):
    """Edit quantity of product in the cart"""

    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get("quantity"))
    cart = request.session.get("cart", {})

    if quantity != cart.get(product_id):
        if quantity > 0:
            cart[product_id] = quantity
            messages.success(
                request,
                f"Updated {product.name} quantity to {cart[product_id]}",
            )
        else:
            cart.pop(product_id)
            messages.success(
                request, f"Removed {quantity} {product.name} from your cart"
            )

        request.session["cart"] = cart

    return redirect(reverse("view_cart"))


def delete_from_cart(request, product_id):
    """Remove a product and its quantity from the cart"""

    try:
        product = get_object_or_404(Product, id=product_id)
        cart = request.session.get("cart", {})

        if product_id in cart:
            del cart[product_id]
            request.session["cart"] = cart
            
            if cart:
                messages.success(
                request, f"Removed all {product.name} from your cart"
                )
            else:
                messages.success(
                request, f"Removed all {product.name} from your cart. Cart is now empty!"
                )

            return redirect(reverse("view_cart"))
            return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f"Error removing item: {e}")

        return HttpResponse(status=500)


def delete_all_cart(request):
    """Remove all products from cart"""

    try:
        cart = request.session.get("cart", {})

        if cart:
            products = Product.objects.filter(id__in=cart.keys())

            request.session["cart"] = {}
            messages.success(request, "All items removed from your cart")

        else:
            messages.info(request, "Your cart is already empty")

        return redirect(reverse("view_cart"))

    except Exception as e:
        messages.error(request, f"Error removing items: {e}")
        return HttpResponse(status=500)
