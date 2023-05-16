from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product, CategoryGroup, SubCategory


def allproducts(request):
    """A view to show all products, including sorting and search queries"""

    products = Product.objects.all()

    context = {
        "products": products,
    }

    return render(request, "products/products.html", context)

def product_detail(request, product_id):
    """A view to show product details of a selected product"""

    product = get_object_or_404(Product, pk=product_id)
   
    context = {
        "product": product,
    }

    return render(request, "products/product_detail.html", context)