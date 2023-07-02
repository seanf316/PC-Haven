from django.test import TestCase, Client
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import UserProfile, Wishlist
from checkout.models import Order
from products.models import Product, CategoryGroup, SubCategory


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
        self.user2 = User.objects.create_user(
            username="john", password="password"
        )
        self.profile, _ = UserProfile.objects.get_or_create(user=self.user)
        self.order = Order.objects.create(
            order_number='12345678', user_profile=self.profile,
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
        self.product1 = Product.objects.create(
            category=self.category,
            sub_category=self.subcategory,
            name="Corsair",
            slug="corsair",
            features="A blue case",
            description="A small case",
            price=99,
            stock_level=2,
            discount=10,
        )

    def test_profile_view(self):
        """
        Test that Profile view renders correct page
        """
        self.client.login(username='sean', password='password')
        response = self.client.get(reverse("profile"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/profile.html")

    def test_update_profile_info(self):
        """
        Test updating Profile information
        """
        self.client.login(username='sean', password='password')
        response = self.client.get(reverse("profile"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/profile.html")
        
        response = self.client.post(reverse('profile'), {
            "default_phone_number": "123456789",
            "default_street_address1": "1 test house",
            "default_street_address2": "1 test street",
            "default_town_or_city": "test city",
            "default_county": "test county",
            "default_postcode": "v12 y934",
            "default_country": "IE",
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("profile"))
        updated_profile = get_object_or_404(UserProfile, user=self.user)
        self.assertEqual(updated_profile.default_phone_number, '123456789')
        self.assertEqual(updated_profile.default_street_address1, '1 test house')
        self.assertEqual(updated_profile.default_street_address2, '1 test street')
        self.assertEqual(updated_profile.default_town_or_city, 'test city')
        self.assertEqual(updated_profile.default_county, 'test county')
        self.assertEqual(updated_profile.default_postcode, 'v12 y934')
        self.assertEqual(updated_profile.default_country, 'IE')

    def test_deleting_user(self):
        """
        Test deleting User/Profile
        """
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 2)
        profile_count = UserProfile.objects.all().count()
        self.assertEqual(profile_count, 2)
        
        self.client.login(username='sean', password='password')
        response = self.client.get(reverse("profile"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/profile.html")
        
        response = self.client.post(reverse('delete_profile', args=['sean']))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("home"))
        
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 1)
        profile_count = UserProfile.objects.all().count()
        self.assertEqual(profile_count, 1)
    
    def test_order_history_view(self):
        """
        Unit tests for order history view
        """
        self.client.login(username='sean', password='password')
        response = self.client.get(
            reverse('order_history',
                    args=[self.order.order_number])
            )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')
        self.assertEqual(response.context['order'], self.order)
        self.assertTrue(response.context['from_profile'])

    def test_add_to_wishlist_authenticated(self):
        """
        Test adding a product to the wishlist when the user is authenticated
        """
        self.client.login(username='sean', password='password')
        response = self.client.get(reverse('add_to_wishlist', args=[self.product.slug]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('product_detail', args=[self.product.slug]))
        
        wishlist = Wishlist.objects.get(user=self.user)
        self.assertIn(self.product, wishlist.products.all())
    
    def test_add_product_to_wishlist_that_contains_product_already(self):
        """
        Test adding a product to the wishlist when the product already exists in wishlist
        """
        self.client.login(username='sean', password='password')
        response = self.client.get(reverse('add_to_wishlist', args=[self.product.slug]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('product_detail', args=[self.product.slug]))
        
        wishlist = Wishlist.objects.get(user=self.user)
        wishlist_count = Wishlist.objects.filter(user=self.user).count()
        self.assertEqual(wishlist_count, 1)
        self.assertIn(self.product, wishlist.products.all())
        
        response = self.client.get(reverse('add_to_wishlist', args=[self.product.slug]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('product_detail', args=[self.product.slug]))
        
        wishlist_count = Wishlist.objects.filter(user=self.user).count()
        self.assertEqual(wishlist_count, 1)
        
    def test_add_product_to_wishlist_not_authenticated(self):
        """
        Test adding a product to the wishlist when not logged in
        """
        response = self.client.get(reverse('add_to_wishlist', args=[self.product.slug]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('products'))

    def test_remove_from_wishlist_authenticated(self):
        """
        Test removing a product from the wishlist when the user is authenticated
        """
        self.client.login(username='sean', password='password')
        response = self.client.get(reverse('add_to_wishlist', args=[self.product.slug]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('product_detail', args=[self.product.slug]))     
        wishlist = Wishlist.objects.get(user=self.user)
        wishlist_count = wishlist.num_products
        self.assertEqual(wishlist_count, 1)
        self.assertIn(self.product, wishlist.products.all())
        
        response = self.client.get(reverse('remove_from_wishlist', args=[self.product.slug]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('product_detail', args=[self.product.slug]))
        
        wishlist = Wishlist.objects.get(user=self.user)
        wishlist_count = wishlist.num_products
        self.assertEqual(wishlist_count, 0)
        self.assertNotIn(self.product, wishlist.products.all())
        
    def test_remove_from_wishlist_when_product_not_in_wishlist(self):
        """
        Test removing a product from the wishlist when product is not in wishlist
        """
        self.client.login(username='sean', password='password')
        response = self.client.get(reverse('add_to_wishlist', args=[self.product.slug]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('product_detail', args=[self.product.slug]))     
        wishlist = Wishlist.objects.get(user=self.user)
        wishlist_count = wishlist.num_products
        self.assertEqual(wishlist_count, 1)
        self.assertIn(self.product, wishlist.products.all())
        
        response = self.client.get(reverse('remove_from_wishlist', args=[self.product1.slug]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('product_detail', args=[self.product1.slug]))
        
    def test_clearing_wishlist(self):
        """
        Test removing all products from the wishlist
        """
        self.client.login(username='sean', password='password')
        response = self.client.get(reverse('add_to_wishlist', args=[self.product.slug]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('product_detail', args=[self.product.slug]))     
        wishlist = Wishlist.objects.get(user=self.user)
        wishlist_count = wishlist.num_products
        self.assertEqual(wishlist_count, 1)
        self.assertIn(self.product, wishlist.products.all())
        
        response = self.client.get(reverse('add_to_wishlist', args=[self.product1.slug]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('product_detail', args=[self.product1.slug]))     
        wishlist = Wishlist.objects.get(user=self.user)
        wishlist_count = wishlist.num_products
        self.assertEqual(wishlist_count, 2)
        self.assertIn(self.product1, wishlist.products.all())

        response = self.client.get(reverse('clear_wishlist'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('profile'))
        
        wishlist = Wishlist.objects.get(user=self.user)
        wishlist_count = wishlist.num_products
        self.assertEqual(wishlist_count, 0)