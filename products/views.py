from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count
from django.db.models.functions import Lower
from .models import Product, CategoryGroup, SubCategory
from django.contrib.auth.models import User
from .forms import ProductForm, CategoryForm, SubcategoryForm


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
            if sortkey == "sub_category":
                sortkey = "sub_category__name"
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


@login_required()
def add_product(request):
    """Add a product to the store"""

    user = request.user

    if not user.is_superuser:
        messages.error(
            request, f"Sorry {user.username}, only store owners can do that."
        )
        return redirect(reverse("home"))

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, "Successfully added product!")
            return redirect(reverse("product_detail", args=[product.id]))
        else:
            messages.error(
                request,
                ("Failed to add product. " "Please ensure the form is valid."),
            )
    else:
        form = ProductForm()

    template = "products/product_management.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """Edit a product in the store"""
    user = request.user

    if not user.is_superuser:
        messages.error(
            request, f"Sorry {user.username}, only store owners can do that."
        )
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated product!")
            return redirect(reverse("product_detail", args=[product.id]))
        else:
            messages.error(
                request,
                (
                    "Failed to update product. "
                    "Please ensure the form is valid."
                ),
            )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f"You are editing {product.name}")

    template = "products/edit_product.html"
    context = {
        "form": form,
        "product": product,
    }

    return render(request, template, context)
