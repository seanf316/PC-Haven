from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q, Count
from .models import Product, CategoryGroup, SubCategory


def allproducts(request):
    """A view to show all products, including sorting and search queries"""

    products = Product.objects.all()
    total_products = Product.objects.count()
    query = None
    categories = None
    subcategories = None
    sort = None
    direction = None

    if request.GET:
        if "sort" in request.GET:
            sortkey = request.GET["sort"]
            sort = sortkey
            if sortkey == "name":
                sortkey = "lower_name"
                products = products.annotate(lower_name=Lower("name"))
            if sortkey == "category":
                sortkey = "category__name"
            if "direction" in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sortkey = f"-{sortkey}"
            products = products.order_by(sortkey)

        if "category" in request.GET:
            categories = request.GET["category"].split(",")
            products = products.filter(category__name__in=categories)
            categories = CategoryGroup.objects.filter(name__in=categories)

        if "sub_category" in request.GET:
            subcategories = request.GET["sub_category"].split(",")
            products = products.filter(sub_category__name__in=subcategories)
            subcategories = SubCategory.objects.filter(name__in=subcategories)

        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(request, "You didn't enter and search criteria")
                return redirect(reverse("products"))

            queries = (
                Q(name__icontains=query)
                | Q(description__icontains=query)
                | Q(information__icontains=query)
                | Q(category__name__icontains=query)
                | Q(sub_category__name__icontains=query)
            )
            products = products.filter(queries)

    paginator = Paginator(products, 12)
    page = request.GET.get("page")
    paginated_products = paginator.get_page(page)
    current_sorting = f"{sort}_{direction}"
    selected_category = request.GET.get("category")

    context = {
        "products": paginated_products,
        "search_query": query,
        "categories": categories,
        "subcategories": subcategories,
        "current_sorting": current_sorting,
        "selected_category": selected_category,
        "total_products": total_products,
    }

    return render(request, "products/products.html", context)


def product_detail(request, product_id):
    """A view to show product details of a selected product"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        "product": product,
    }

    return render(request, "products/product_detail.html", context)
