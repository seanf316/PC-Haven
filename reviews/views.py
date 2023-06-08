from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from products.models import Product
from django.contrib.auth.models import User
from .models import Review
from .forms import ReviewForm


@login_required()
def add_review(request, product_id):
    """Add a review on a Product"""

    user = request.user
    product = get_object_or_404(Product, pk=product_id)

    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = user
            review = form.save()
            messages.success(request, f"Successfully added review.")
            return redirect(reverse("product_detail", args=[product_id]))
        else:
            messages.error(
                request,
                ("Failed to add review. Please review your form."),
            )
    else:
        form = ReviewForm()

    template = "reviews/review.html"
    context = {
        "form": form,
        "product": product,
    }

    return render(request, template, context)
