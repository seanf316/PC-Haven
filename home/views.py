from django.shortcuts import render
from products.models import Product


def home(request):
    """A view to return the home page"""
    featured_products = Product.objects.filter(featured_product=True)
    latest_products = Product.objects.order_by("-created_on")[:10]
    sale_products = Product.objects.filter(has_sale=True)
    context = {
        "featured_products": featured_products,
        "latest_products": latest_products,
        "sale_products": sale_products,
    }
    return render(request, "home/index.html", context)


def privacy(request):
    """A view to return the privacy policy page"""
    return render(request, "home/privacy_policy.html")


def terms(request):
    """A view to return the terms and conditions page"""
    return render(request, "home/terms.html")


def faq(request):
    """A view to return the faq page"""
    return render(request, "home/faq.html")
