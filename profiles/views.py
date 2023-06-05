from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UserForm, UserProfileForm


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
