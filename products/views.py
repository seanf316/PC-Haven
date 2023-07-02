from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Avg
from django.db.models.functions import Lower
from .models import Product, CategoryGroup, SubCategory
from .forms import ProductForm
from profiles.models import Wishlist
from reviews.models import Review


def allproducts(request):
    """A view to show all products, including sorting and search queries"""

    products = Product.objects.all()
    user = request.user
    total_products = Product.objects.count()
    query = None
    categories = None
    subcategories = None
    sort = None
    direction = None

    if user.is_authenticated:
        wishlist, created = Wishlist.objects.get_or_create(user=user)
    else:
        wishlist = None

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
                | Q(features__icontains=query)
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
        "wishlist": wishlist,
    }

    return render(request, "products/products.html", context)


def product_detail(request, slug):
    """A view to show product details of a selected product"""

    product = get_object_or_404(Product, slug=slug)
    user = request.user
    reviews = Review.objects.filter(product=product)
    rating_avg = reviews.aggregate(Avg("rating"))

    if user.is_authenticated:
        wishlist, created = Wishlist.objects.get_or_create(user=user)
        user_review = Review.objects.filter(user=user, product=product)
    else:
        wishlist = None
        user_review = None

    context = {
        "product": product,
        "wishlist": wishlist,
        "reviews": reviews,
        "user_review": user_review,
        "rating_avg": rating_avg,
    }

    return render(request, "products/product_detail.html", context)


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
            messages.success(
                request, f"Successfully added {product.name} to inventory!"
            )
            return redirect(reverse("product_detail", args=[product.slug]))
        else:
            messages.error(
                request,
                ("Failed to add product. " "Please ensure the form is valid."),
            )
    else:
        form = ProductForm()

    template = "products/add_product.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, slug):
    """Edit a product in the store"""
    user = request.user

    if not user.is_superuser:
        messages.error(
            request, f"Sorry {user.username}, only store owners can do that."
        )
        return redirect(reverse("home"))

    product = get_object_or_404(Product, slug=slug)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f"Successfully updated {product.name}!")
            return redirect(reverse("product_detail", args=[product.slug]))
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
        messages.info(
            request, f"{user.username} you are editing {product.name}"
        )

    template = "products/edit_product.html"
    context = {
        "form": form,
        "product": product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, slug):
    """Delete a product from the store"""
    user = request.user

    if not user.is_superuser:
        messages.error(
            request, f"Sorry {user.username}, only store owners can do that."
        )
        return redirect(reverse("home"))

    product = get_object_or_404(Product, slug=slug)
    product.delete()
    messages.success(request, f"Product {product.name} has been deleted!")
    return redirect(reverse("products"))
