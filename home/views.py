from django.shortcuts import render
from products.models import Product


def home(request):
    """A view to return the home page"""
    featured_products = Product.objects.filter(featured_product=True)
    latest_products = Product.objects.order_by("-created_on")[:10]
    print(featured_products)
    context = {
        "featured_products": featured_products,
        "latest_products": latest_products,
    }
    return render(request, "home/index.html", context)
