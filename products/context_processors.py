from .models import CategoryGroup, SubCategory


def getlinks(request):
    all_categories = CategoryGroup.objects.all().order_by('name')

    return {"allcategories": all_categories}
