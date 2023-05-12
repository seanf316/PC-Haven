from django.shortcuts import render
from .models import Product, CategoryGroup, SubCategory


def allproducts(request):
    """A view to show all prdoucts, including sorting and search queries"""

    products = Product.objects.all()

    context = {
        "products": products,
    }

    return render(request, "products/products.html", context)
