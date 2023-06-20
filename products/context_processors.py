from .models import CategoryGroup


def getlinks(request):
    """A view to retrieve all the Categories and order by name"""
    all_categories = CategoryGroup.objects.all().order_by("name")

    return {"allcategories": all_categories}
