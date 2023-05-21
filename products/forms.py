from django import forms
from .widgets import CustomClearableFileInput
from django_summernote.widgets import SummernoteWidget
from .models import Product, CategoryGroup, SubCategory


class CategoryForm(forms.ModelForm):
    class Meta:
        model = CategoryGroup
        fields = "__all__"


class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = "__all__"


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        exclude = ["sku", "in_stock", "category"]

        widgets = {
            "description": SummernoteWidget(),
            "information": SummernoteWidget(),
            "image": CustomClearableFileInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        subcategories = SubCategory.objects.all()
        sub_category_friendly_names = [
            (c.id, c.get_friendly_name()) for c in subcategories
        ]
        self.fields["sub_category"].choices = sub_category_friendly_names
