from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
import stripe
from pchaven.settings import (
    STRIPE_PUBLIC_KEY,
    STRIPE_SECRET_KEY,
    STRIPE_CURRENCY,
    STRIPE_WH_SECRET,
)
from .forms import OrderForm
from cart.contexts import cart_contents


def checkout(request):
    user = request.user
    cart = request.session.get("cart", {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse("products"))

    current_cart = cart_contents(request)
    total = current_cart["grand_total"]
    stripe_total = round(total * 100)
    stripe.api_key = STRIPE_SECRET_KEY
    intent = stripe.PaymentIntent.create(
        amount=stripe_total, currency=STRIPE_CURRENCY
    )

    order_form = OrderForm()

    if not STRIPE_PUBLIC_KEY:
        messages.warning(self.request, "Stripe Public Key Missing!!")

    template = "checkout/checkout.html"
    context = {
        "order_form": order_form,
        "stripe_public_key": STRIPE_PUBLIC_KEY,
        "client_secret": intent.client_secret,
    }

    return render(request, template, context)
