from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from products.models import CategoryGroup, SubCategory, Product


class TestCartViews(TestCase):
    """
    Testing for cart views
    """

    def setUp(self):
        """
        Setup method
        """
        self.client = Client()
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

    def test_cart_page_renders(self):
        """
        Test that view_cart view renders correct page
        """
        response = self.client.get(reverse("view_cart"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "cart/cart.html")

    def test_add_to_cart_view(self):
        """
        Test for adding product to cart
        """
        response = self.client.post(
            reverse("add_to_cart", args=[self.product.id]),
            {
                "quantity": 1,
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, reverse("product_detail", args=[self.product.id])
        )
        cart = self.client.session.get("cart", {})
        self.assertEqual(cart.get(str(self.product.id)), 1)

        response = self.client.post(
            reverse("add_to_cart", args=[self.product.id]), {"quantity": 2}
        )
        self.assertEqual(response.status_code, 302)  # Expect a redirect
        self.assertRedirects(
            response, reverse("product_detail", args=[self.product.id])
        )
        cart = self.client.session.get("cart", {})
        self.assertEqual(cart.get(str(self.product.id)), 3)

    def test_edit_cart_view(self):
        """
        Test for editing the cart
        """
        response = self.client.post(
            reverse("add_to_cart", args=[self.product.id]),
            {
                "quantity": 1,
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, reverse("product_detail", args=[self.product.id])
        )
        cart = self.client.session.get("cart", {})
        self.assertEqual(cart.get(str(self.product.id)), 1)

        response = self.client.post(
            reverse("edit_cart", args=[self.product.id]), {"quantity": 2}
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("view_cart"))
        updated_cart = self.client.session.get("cart", {})
        self.assertEqual(updated_cart.get(str(self.product.id)), 2)

        response = self.client.post(
            reverse("edit_cart", args=[self.product.id]), {"quantity": 0}
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("view_cart"))
        updated_cart = self.client.session.get("cart", {})
        self.assertEqual(updated_cart.get(str(self.product.id)), None)

    def test_delete_product_from_cart_view(self):
        """
        Test for editing the cart
        """
        response = self.client.post(
            reverse("add_to_cart", args=[self.product.id]),
            {
                "quantity": 1,
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, reverse("product_detail", args=[self.product.id])
        )
        cart = self.client.session.get("cart", {})
        self.assertEqual(cart.get(str(self.product.id)), 1)

        response = self.client.post(
            reverse("delete_from_cart", args=[self.product.id]),
            {
                "quantity": 1,
            },
        )
        cart = self.client.session.get("cart", {})
        self.assertNotIn(str(self.product.id), cart)
