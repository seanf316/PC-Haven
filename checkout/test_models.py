from django.test import TestCase
from django.contrib.auth.models import User
from .models import Order, OrderLineItem
from products.models import Product, CategoryGroup, SubCategory
from profiles.models import UserProfile


class TestOrderModel(TestCase):
    """
    Unit Tests For Order model
    """

    def setUp(self):
        """
        setup method
        """
        self.user = User.objects.create_user(
            username="sean", email="finn@test.com", password="password"
        )
        self.profile, _ = UserProfile.objects.get_or_create(user=self.user)
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
        self.order = Order.objects.create(
            user_profile=self.profile,
            full_name="sean finn",
            phone_number="123456789",
            street_address1="1 test house",
            street_address2="1 test street",
            town_or_city="test city",
            county="test county",
            postcode="v12 y934",
            country="IE",
        )
        self.order_line_item = OrderLineItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=2,
            lineitem_total=200,
        )

    def test_order_number_generated(self):
        """
        Test that the order number is generated when saving an Order instance
        if it hasn't been set already.
        """
        order = self.order
        self.assertIsNotNone(order.order_number)

    def test_order_str_representation(self):
        """
        Test the Order model's attributes
        """
        self.assertEqual(str(self.order), self.order.order_number)

    def test_order_line_item_str_representation(self):
        """
        Test the OrderLineItem model's attributes
        """
        expected_str = (
            f"SKU {self.product.sku} on order {self.order.order_number}"
        )
        self.assertEqual(str(self.order_line_item), expected_str)
