from django.test import TestCase, Client
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import CategoryGroup, SubCategory, Product


class ProductViewsTestCase(TestCase):
    """
    Test Product Views
    """

    def setUp(self):
        """
        Setup Method
        """
        self.client = Client()
        self.user = User.objects.create_user(
            username="sean", password="password"
        )
        self.superuser = User.objects.create_user(
            username="supersean", password="superpassword", is_superuser=True
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
        self.product.sku = self.product.generate_sku()
        self.product.save()

    def test_allproducts_view(self):
        """
        Test that All Products view renders correct page
        """
        response = self.client.get(reverse("products"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/products.html")

    def test_allproducts_view_sorting(self):
        """
        Test product sorting
        """
        response = self.client.get(
            reverse("products"), {"sort": "sub_category"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/products.html")

    def test_allproducts_search(self):
        """
        Test product searching
        """
        response = self.client.get(reverse("products"), {"q": "nzxt"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/products.html")

    def test_allproducts_search_no_query(self):
        """
        Test product searching with no query
        """
        response = self.client.get(reverse("products"), {"q": ""})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("products"))

    def test_product_detail_view(self):
        """
        Test that All Products view renders correct page
        """
        response = self.client.get(
            reverse("product_detail", args=[self.product.slug])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/product_detail.html")

    def test_add_product(self):
        """
        Test adding a product
        """
        product_count = Product.objects.all().count()
        self.assertEqual(product_count, 1)

        self.client.login(username="supersean", password="superpassword")
        response = self.client.get(reverse("add_product"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/add_product.html")

        product_data = {
            "category": self.category.id,
            "sub_category": self.subcategory.id,
            "name": "Corsair",
            "slug": "corsair",
            "sku": "pp-12334456",
            "features": "An old case",
            "description": "A small case",
            "price": 100,
            "stock_level": 10,
            "discount": 10,
        }

        response = self.client.post(
            reverse("add_product"),
            data=product_data,
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, reverse("product_detail", args=[product_data["slug"]])
        )

        product_count = Product.objects.all().count()
        self.assertEqual(product_count, 2)

    def test_add_product_invalid(self):
        """
        Test adding a product with invalid data
        """
        product_count = Product.objects.all().count()
        self.assertEqual(product_count, 1)

        self.client.login(username="supersean", password="superpassword")
        response = self.client.get(reverse("add_product"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/add_product.html")

        product_data = {
            "category": self.category.id,
            "sub_category": self.subcategory.id,
            "name": "",
            "slug": "corsair",
            "sku": "pp-12334456",
            "features": "An old case",
            "description": "A small case",
            "price": 100,
            "stock_level": 10,
            "discount": 10,
        }

        response = self.client.post(
            reverse("add_product"),
            data=product_data,
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/add_product.html")

        product_count = Product.objects.all().count()
        self.assertEqual(product_count, 1)

    def test_add_product_no_superuser(self):
        """
        Test adding a product if not superuser
        """
        self.client.login(username="sean", password="password")
        response = self.client.get(reverse("add_product"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("home"))

    def test_edit_product(self):
        """
        Test edit a product
        """
        self.client.login(username="supersean", password="superpassword")
        response = self.client.get(
            reverse("edit_product", args=[self.product.slug])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/edit_product.html")
        self.assertEqual(self.product.name, "NZXT")
        self.assertEqual(self.product.features, "A new case")

        product_data = {
            "category": self.category.id,
            "sub_category": self.subcategory.id,
            "name": "corsair",
            "slug": "corsair",
            "sku": "pp-12334456",
            "features": "An old case",
            "description": "A small case",
            "price": 100,
            "stock_level": 10,
            "discount": 10,
        }

        response = self.client.post(
            reverse("edit_product", args=[self.product.slug]),
            data=product_data,
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, reverse("product_detail", args=[product_data["slug"]])
        )

        updated_product = get_object_or_404(Product, slug=product_data["slug"])
        self.assertEqual(updated_product.name, "corsair")
        self.assertEqual(updated_product.features, "An old case")

    def test_edit_product_invalid(self):
        """
        Test editing a product with invalid data
        """
        self.client.login(username="supersean", password="superpassword")
        response = self.client.get(
            reverse("edit_product", args=[self.product.slug])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/edit_product.html")

        product_data = {
            "category": self.category.id,
            "sub_category": self.subcategory.id,
            "name": "",
            "slug": "corsair",
            "sku": "pp-12334456",
            "features": "An old case",
            "description": "A small case",
            "price": 100,
            "stock_level": 10,
            "discount": 10,
        }

        response = self.client.post(
            reverse("edit_product", args=[self.product.slug]),
            data=product_data,
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/edit_product.html")

    def test_edit_product_no_superuser(self):
        """
        Test editing a product with invalid data
        """
        self.client.login(username="sean", password="password")
        response = self.client.get(
            reverse("edit_product", args=[self.product.slug])
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("home"))

    def test_delete_product(self):
        """
        Test delete a product
        """
        product_count = Product.objects.all().count()
        self.assertEqual(product_count, 1)
        self.client.login(username="supersean", password="superpassword")

        response = self.client.post(
            reverse("delete_product", args=[self.product.slug])
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("products"))

        product_count = Product.objects.all().count()
        self.assertEqual(product_count, 0)

    def test_delete_product_no_super(self):
        """
        Test delete a product without being superuser
        """
        self.client.login(username="sean", password="password")

        response = self.client.post(
            reverse("delete_product", args=[self.product.slug])
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("home"))
