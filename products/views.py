from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, CategoryGroup, SubCategory


def allproducts(request):
    """A view to show all products, including sorting and search queries"""

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter and search criteria")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(information__icontains=query) | Q(category__name__icontains=query) | Q(sub_category__name__icontains=query)
            products = products.filter(queries)
    context = {
        "products": products,
        "search_query": query,
    }

    return render(request, "products/products.html", context)

def product_detail(request, product_id):
    """A view to show product details of a selected product"""

    product = get_object_or_404(Product, pk=product_id)
   
    context = {
        "product": product,
    }

    return render(request, "products/product_detail.html", context)