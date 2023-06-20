from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404,
    HttpResponse,
)
from django.views.decorators.http import require_POST
from django.contrib import messages
from products.models import Product
from .models import OrderLineItem, Order
from .forms import OrderForm
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from pchaven.settings import (
    STRIPE_PUBLIC_KEY,
    STRIPE_SECRET_KEY,
    STRIPE_CURRENCY,
)
from cart.contexts import cart_contents
import stripe
import json


@require_POST
def cache_checkout_data(request):
    """Stores the checkout data and stores it in the user's session"""
    try:
        pid = request.POST.get("client_secret").split("_secret")[0]
        stripe.api_key = STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(
            pid,
            metadata={
                "cart": json.dumps(request.session.get("cart", {})),
                "save_info": request.POST.get("save_info"),
                "username": request.user,
            },
        )
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(
            request,
            "Sorry, your payment cannot be \
            processed right now. Please try again later.",
        )
        return HttpResponse(content=e, status=400)


def checkout(request):
    """
    A view that renders the checkout page and retrieves the
    payment form data from the profile if one is present
    """
    if request.method == "POST":
        user = request.user
        cart = request.session.get("cart", {})
        form_data = {
            "full_name": request.POST["full_name"],
            "email": request.POST["email"],
            "phone_number": request.POST["phone_number"],
            "street_address1": request.POST["street_address1"],
            "street_address2": request.POST["street_address2"],
            "town_or_city": request.POST["town_or_city"],
            "county": request.POST["county"],
            "postcode": request.POST["postcode"],
            "country": request.POST["country"],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get("client_secret").split("_secret")[0]
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            order.save()
            for product_id, product_quantity in cart.items():
                try:
                    product = Product.objects.get(id=product_id)

                    if product.stock_level > 0:
                        product.stock_level -= product_quantity
                        product.save()
                    else:
                        if user.is_authenticated:
                            messages.error(
                                request,
                                (
                                    f"Sorry {user.username}, we are currently"
                                    f" out of stock of {product.name}. Please"
                                    " remove this item from your cart and try"
                                    " again later.",
                                ),
                            )
                        else:
                            messages.error(
                                request,
                                (
                                    "Sorry, we are currently out of stock of"
                                    f" {product.name}. Please remove this item"
                                    " from your cart and try again later."
                                ),
                            )
                        order.delete()
                        return redirect(reverse("view_cart"))

                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=product_quantity,
                    )
                    order_line_item.save()
                except Product.DoesNotExist:
                    if user.is_authenticated:
                        messages.error(
                            request,
                            (
                                f"Sorry {user.username} one of the products -"
                                f" {product.name} in your cart was not found "
                                "in our database. Please contact us for "
                                "assistance!"
                            ),
                        )
                    else:
                        messages.error(
                            request,
                            (
                                f"Sorry one of the products - {product.name} "
                                "in your cart was not found in our database. "
                                "Please contact us for assistance!"
                            ),
                        )
                    order.delete()
                    return redirect(reverse("view_cart"))

            request.session["save_info"] = "save-info" in request.POST
            return redirect(
                reverse("checkout_success", args=[order.order_number])
            )
        else:
            messages.error(
                request,
                "There was an error with your form. \
                Please double check your information.",
            )
    else:
        user = request.user
        cart = request.session.get("cart", {})
        if not cart:
            messages.error(
                request, "There's nothing in your cart at the moment"
            )
            return redirect(reverse("products"))

        current_cart = cart_contents(request)
        total = current_cart["grand_total"]
        stripe_total = round(total * 100)
        stripe.api_key = STRIPE_SECRET_KEY
        intent = stripe.PaymentIntent.create(
            amount=stripe_total, currency=STRIPE_CURRENCY
        )

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=user)
                order_form = OrderForm(
                    initial={
                        "full_name": profile.user.get_full_name(),
                        "email": profile.user.email,
                        "phone_number": profile.default_phone_number,
                        "street_address1": profile.default_street_address1,
                        "street_address2": profile.default_street_address2,
                        "town_or_city": profile.default_town_or_city,
                        "county": profile.default_county,
                        "postcode": profile.default_postcode,
                        "country": profile.default_country,
                    }
                )
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not STRIPE_PUBLIC_KEY:
        messages.warning(request, "Stripe Public Key Missing!!")

    template = "checkout/checkout.html"
    context = {
        "order_form": order_form,
        "stripe_public_key": STRIPE_PUBLIC_KEY,
        "client_secret": intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    user = request.user
    save_info = request.session.get("save_info")
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                "default_phone_number": order.phone_number,
                "default_street_address1": order.street_address1,
                "default_street_address2": order.street_address2,
                "default_town_or_city": order.town_or_city,
                "default_county": order.county,
                "default_postcode": order.postcode,
                "default_country": order.country,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

        messages.success(
            request,
            f"Thank You {user.username}! Order successfully processed! \
            Your order number is {order_number}. A confirmation \
            email will be sent to {order.email}.",
        )
    else:
        messages.success(
            request,
            f"Thank You! Order successfully processed! \
            Your order number is {order_number}. A confirmation \
            email will be sent to {order.email}.",
        )

    if "cart" in request.session:
        del request.session["cart"]

    template = "checkout/checkout_success.html"
    context = {
        "order": order,
    }

    return render(request, template, context)
