from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile
from checkout.models import Order
from .forms import UserForm, UserProfileForm


@login_required()
def profile(request):
    """Display the user's profile."""
    user = get_object_or_404(User, username=request.user)
    profile = get_object_or_404(UserProfile, user=user)

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
        "userform": userform,
        "profileform": profileform,
        "orders": orders,
        "on_profile_page": True,
    }

    return render(request, template, context)


@login_required()
def order_history(request, order_number):
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
