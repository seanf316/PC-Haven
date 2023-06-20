from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
    reverse,
    HttpResponseRedirect,
    Http404,
)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from checkout.models import Order
from products.models import Product
from .models import UserProfile, Wishlist
from .forms import UserForm, UserProfileForm


@login_required()
def profile(request):
    """
    Display the User's profile
    """
    user = get_object_or_404(User, username=request.user)
    profile = get_object_or_404(UserProfile, user=user)
    wishlist, created = Wishlist.objects.get_or_create(user=user)

    if request.method == "POST":
        userform = UserForm(request.POST, instance=user)
        profileform = UserProfileForm(request.POST, instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            profileform.save()
            messages.success(request, "Profile updated successfully")
            return redirect(("profile"))

    userform = UserForm(instance=user)
    profileform = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = "profiles/profile.html"
    context = {
        "profile": profile,
        "userform": userform,
        "profileform": profileform,
        "orders": orders,
        "wishlist": wishlist,
        "on_profile_page": True,
    }

    return render(request, template, context)


@login_required()
def delete_profile(request, username):
    """
    Querys the database for the User that matches profile user
    and deletes user & profile
    """
    user = get_object_or_404(User, username=request.user)
    profile = get_object_or_404(UserProfile, user=user)

    if user != profile:
        messages.success(
            request, "You are not authorised to delete this Profile."
        )
        return redirect(("profile"))

    if request.method == "POST":
        logout(request)
        user.delete()
        messages.success(
            request, "Sorry to see you go, your Account has been deleted."
        )
        return redirect(reverse("home"))

    context = {"username": username}
    return render(request, "profiles/edit_profile.html", context)


@login_required()
def order_history(request, order_number):
    """Display the User's Order History"""
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(
        request,
        (
            f"This is a past confirmation for order number {order_number}. "
            "A confirmation email was sent on the order date."
        ),
    )

    template = "checkout/checkout_success.html"
    context = {
        "order": order,
        "from_profile": True,
    }

    return render(request, template, context)


def add_to_wishlist(request, slug):
    """
    Add Product to User Wishlist
    """
    product = get_object_or_404(Product, slug=slug)

    if not request.user.is_authenticated:
        messages.info(
            request,
            "You will need to Sign Up or Login to add Products to Wislist.",
        )
        return redirect("products")

    try:
        wishlist = get_object_or_404(Wishlist, user=request.user.id)
    except Http404:
        wishlist = Wishlist.objects.create(user=request.user)

    if product in wishlist.products.all():
        messages.info(request, f"{product.name} is already on your Wishlist!")
    else:
        wishlist.products.add(product)
        messages.success(
            request, f"{product.name} has been added to your Wishlist!"
        )

    redirect_url = request.META.get(
        "HTTP_REFERER", (reverse("product_detail", args=[product.slug]))
    )

    return HttpResponseRedirect(redirect_url)


@login_required
def remove_from_wishlist(request, slug):
    """
    Remove a Product from User Wishlist
    """
    product = get_object_or_404(Product, slug=slug)
    wishlist = Wishlist.objects.get(user=request.user)

    if product in wishlist.products.all():
        wishlist.products.remove(product)
        messages.success(
            request, f"{product.name} has been removed from your Wishlist!"
        )
    else:
        messages.error(request, f"{product.name} is not in your Wishlist!")

    redirect_url = request.META.get(
        "HTTP_REFERER", (reverse("product_detail", args=[product.slug]))
    )

    return HttpResponseRedirect(redirect_url)


@login_required()
def clear_wishlist(request):
    """
    Remove all Products from User Wishlist
    """
    wishlist = Wishlist.objects.get(user=request.user)

    products = wishlist.products.all()

    for product in products:
        wishlist.products.remove(product)

    messages.success(request, "Your wishlist has been cleared!")

    redirect_url = request.META.get("HTTP_REFERER", reverse("profile"))

    return HttpResponseRedirect(redirect_url)
