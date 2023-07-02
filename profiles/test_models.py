from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile, Wishlist
from products.models import CategoryGroup, SubCategory, Product


class TestUserProfileModel(TestCase):
    """
    Testing UserProfile Model
    """

    def setUp(self):
        """
        Sets the UserProfile Object with required attributes
        """
        self.user = User.objects.create_user(
            username="sean", email="finn@test.com", password="password"
        )
        self.profile, _ = UserProfile.objects.get_or_create(user=self.user)
        self.expected_str = str(self.user.username)

    def test_useprofile_model(self):
        """
        Tests the UserProfile model's attributes
        """
        self.assertEqual(self.profile.user.username, "sean")
        self.assertEqual(str(self.profile), self.expected_str)

class TestWishlistModel(TestCase):
    """
    Testing Wishlist Model
    """

    def setUp(self):
        """
        Sets the Wishlist Object with required attributes
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
        self.wishlist = Wishlist.objects.create(user=self.user)
        self.expected_str = str(f"{self.user.username}'s Wishlist")

    def test_num_products(self):
        """
        Tests the number of products in wishlist
        """
        self.wishlist.products.add(self.product)

        self.assertEqual(self.wishlist.num_products, 1)

    def test_wishlist_model(self):
        """
        Tests the Wishlist model's attributes
        """
        self.assertEqual(str(self.wishlist), self.expected_str)