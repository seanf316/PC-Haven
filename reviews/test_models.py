from django.test import TestCase
from django.contrib.auth.models import User
from .models import Review
from products.models import Product, CategoryGroup, SubCategory


class TestReviewModel(TestCase):
    """
    Testing Review Model
    """

    def setUp(self):
        """
        Sets the Review Object with required attributes
        """
        self.user = User.objects.create_user(
            username="sean", email="finn@test.com", password="password"
        )
        self.category = CategoryGroup.objects.create(
            name="Cases", friendly_name="cases"
        )
        self.subcategory = SubCategory.objects.create(
            name="Full Tower", friendly_name="full_tower"
        )
        self.product = Product.objects.create(
            category=self.category,
            sub_category=self.subcategory,
            name="NZXT",
            slug="nzxt",
            features="A new case",
            description="A big case",
            price=100,
            stock_level=1,
            discount=10,
        )
        self.review = Review.objects.create(
            user=self.user,
            product=self.product,
            review="Good product",
            rating=5,
        )
        self.expected_str = str(f"{self.user.username} - {self.product.name}")

    def test_review_model(self):
        """
        Tests the Review model's attributes
        """
        self.assertEqual(self.review.user.username, "sean")
        self.assertEqual(self.review.product.name, "NZXT")
        self.assertEqual(self.review.review, "Good product")
        self.assertEqual(self.review.rating, 5)
        self.assertEqual(str(self.review), self.expected_str)
