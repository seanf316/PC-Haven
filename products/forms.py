from django import forms
from .widgets import CustomClearableFileInput
from django_summernote.widgets import SummernoteWidget
from .models import Product, CategoryGroup, SubCategory


class CategoryForm(forms.ModelForm):
    """
    Form to add new Categories
    """

    class Meta:
        """
        Define model, form fields and widgets
        """

        model = CategoryGroup
        fields = "__all__"


class SubcategoryForm(forms.ModelForm):
    """
    Form to add new Sub-Categories
    """

    class Meta:
        """
        Define model, form fields and widgets
        """

        model = SubCategory
        fields = "__all__"


class ProductForm(forms.ModelForm):
    """
    Form to add new Products
    """

    class Meta:
        """
        Define model, form fields and widgets
        """

        model = Product
        fields = "__all__"
        exclude = ["sku", "in_stock", "image_url"]

        labels = {
            "featured_product": "Featured Product (Tick to confirm)",
            "has_sale": "Place Product on Sale (Tick to confirm)",
        }

        widgets = {
            "features": SummernoteWidget(),
            "description": SummernoteWidget(),
            "image": CustomClearableFileInput(),
        }

    def __init__(self, *args, **kwargs):
        """
        Retrieves the Category/Subcategory friendly names and
        sets them as the choices in select fields
        """
        super().__init__(*args, **kwargs)
        categories = CategoryGroup.objects.all()
        category_friendly_names = [
            (c.id, c.get_friendly_name()) for c in categories
        ]
        subcategories = SubCategory.objects.all()
        sub_category_friendly_names = [
            (c.id, c.get_friendly_name()) for c in subcategories
        ]
        self.fields["category"].choices = category_friendly_names
        self.fields["sub_category"].choices = sub_category_friendly_names
