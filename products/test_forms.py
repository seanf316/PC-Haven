from django.test import TestCase
from .forms import ProductForm
from .models import CategoryGroup, SubCategory


class TestProductForm(TestCase):
    """Testing Product Form"""

    def setUp(self):
        """
        Setup Method
        """
        self.category = CategoryGroup.objects.create(name="Cases")
        self.sub_category = SubCategory.objects.create(name="Full Tower")

    def test_productform_valid(self):
        """Test Product form is valid"""
        form = ProductForm(
            {
                "category": self.category,
                "sub_category": self.sub_category,
                "name": "NZXT",
                "sku": "abcdefg",
                "slug": "nzxt",
                "features": "A new case",
                "description": "A big case",
                "price": 12,
                "stock_level": 1,
                "discount": 0,
            }
        )
        self.assertTrue(form.is_valid(), form.errors)

    def test_productform_not_valid(self):
        """Test Product form is not valid"""
        form = ProductForm(
            {
                "category": self.category.id,
                "sub_category": self.sub_category.id,
                "name": "",
                "sku": "abcdefg",
                "slug": "nzxt",
                "features": "A new case",
                "description": "A big case",
                "price": 12,
                "stock_level": 1,
                "discount": 0,
            }
        )
        self.assertIn("name", form.errors.keys())
        self.assertEqual(form.errors["name"][0], "This field is required.")
        self.assertFalse(form.is_valid())

    def test_productform_title_above_max_characters(self):
        """Product form name field exceeds 254 characters"""
        form = ProductForm(
            {
                "category": "Cases",
                "sub_category": "Full Tower",
                "name": str("a" * 255),
                "sku": "abcdefg",
                "slug": "nzxt",
                "features": "A new case",
                "description": "A big case",
                "price": 12,
                "stock_level": 1,
                "discount": 0,
            }
        )
        self.assertIn("name", form.errors.keys())
        self.assertEqual(
            form.errors["name"][0],
            "Ensure this value has at most 254 characters (it has 255).",
        )
        self.assertFalse(form.is_valid())
