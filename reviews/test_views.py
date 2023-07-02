from django.test import TestCase, Client
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Review
from products.models import Product, CategoryGroup, SubCategory

class TestReviewViews(TestCase):
    """
    Testing Review Views
    """

    def setUp(self):
        """
        Setup creates user, profile, movie and logs user in
        """
        self.client = Client()
        self.user = User.objects.create_user(
            username="sean", email="finn@test.com", password="password"
        )
        self.user1 = User.objects.create_user(
            username="john", email="flynn@test.com", password="password"
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

    def test_add_review(self):
        """
        Test adding a review for a product
        """
        review_count = Review.objects.all().count()
        self.assertEqual(review_count, 1)

        self.client.login(username="sean", password="password")
        response = self.client.get(reverse("add_review", args=[self.product.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "reviews/review.html")

        review_data = {
            "review": "Bad product",
            "rating": 1,
        }

        response = self.client.post(
            reverse("add_review", args=[self.product.slug]),
            data=review_data,
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, reverse("product_detail", args=[self.product.slug])
        )

        review_count = Review.objects.all().count()
        self.assertEqual(review_count, 2)
        
    def test_add_review_invalid(self):
        """
        Test adding a review for a product
        """
        review_count = Review.objects.all().count()
        self.assertEqual(review_count, 1)

        self.client.login(username="sean", password="password")

        review_data = {
            "review": "Bad product",
            "rating": 10,
        }

        response = self.client.post(
            reverse("add_review", args=[self.product.slug]),
            data=review_data,
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "reviews/review.html")

        review_count = Review.objects.all().count()
        self.assertEqual(review_count, 1)

    def test_edit_review(self):
        """
        Test edit a review
        """
        self.client.login(username="sean", password="password")
        response = self.client.get(reverse("edit_review", args=[self.product.slug, self.review.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "reviews/edit_review.html")
        self.assertEqual(self.review.review, "Good product")
        self.assertEqual(self.review.rating, 5)

        review_data = {
            "review": "Bad product",
            "rating": 1,
        }

        response = self.client.post(
            reverse("edit_review", args=[self.product.slug, self.review.id]),
            data=review_data,
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, reverse("product_detail", args=[self.product.slug])
        )

        updated_review = get_object_or_404(Review, review=review_data["review"])
        self.assertEqual(updated_review.review, review_data["review"])
        self.assertEqual(updated_review.rating, review_data["rating"])
        
    def test_edit_review_invalid(self):
        """
        Test editing a review with invalid data
        """
        self.client.login(username="sean", password="password")
        response = self.client.get(reverse("edit_review", args=[self.product.slug, self.review.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "reviews/edit_review.html")
        self.assertEqual(self.review.review, "Good product")
        self.assertEqual(self.review.rating, 5)

        review_data = {
            "review": "Bad product",
            "rating": 10,
        }

        response = self.client.post(
            reverse("edit_review", args=[self.product.slug, self.review.id]),
            data=review_data,
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "reviews/edit_review.html")
    
    def test_edit_review_not_review_owner(self):
        """
        Test edit a review not as the review owner
        """
        review_count = Review.objects.all().count()
        self.assertEqual(review_count, 1)

        self.client.login(username="sean", password="password")
        response = self.client.get(reverse("add_review", args=[self.product.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "reviews/review.html")

        review_data = {
            "review": "Bad product",
            "rating": 1,
        }

        response = self.client.post(
            reverse("add_review", args=[self.product.slug]),
            data=review_data,
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, reverse("product_detail", args=[self.product.slug])
        )

        review_count = Review.objects.all().count()
        self.assertEqual(review_count, 2)

        new_review = Review.objects.latest("id")
        self.assertEqual(new_review.review, review_data["review"])

        self.client.logout()

        self.client.login(username="john", password="password")

        review = Review.objects.latest("id")
        response = self.client.get(reverse("edit_review", args=[self.product.slug, self.review.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, reverse("product_detail", args=[self.product.slug])
        )
    
    def test_delete_review(self):
        """
        Test delete a review
        """
        review_count = Review.objects.all().count()
        self.assertEqual(review_count, 1)
        self.client.login(username="sean", password="password")

        response = self.client.post(
            reverse("delete_review", args=[self.product.slug, self.review.id])
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, reverse("product_detail", args=[self.product.slug])
        )

        review_count = Review.objects.all().count()
        self.assertEqual(review_count, 0)
        
    def test_delete_review_not_review_owner(self):
        """
        Test delete a review when not review owner
        """
        review_count = Review.objects.all().count()
        self.assertEqual(review_count, 1)

        self.client.login(username="sean", password="password")
        response = self.client.get(reverse("add_review", args=[self.product.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "reviews/review.html")

        review_data = {
            "review": "Bad product",
            "rating": 1,
        }

        response = self.client.post(
            reverse("add_review", args=[self.product.slug]),
            data=review_data,
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, reverse("product_detail", args=[self.product.slug])
        )

        review_count = Review.objects.all().count()
        self.assertEqual(review_count, 2)

        new_review = Review.objects.latest("id")
        self.assertEqual(new_review.review, review_data["review"])

        self.client.logout()

        self.client.login(username="john", password="password")

        review = Review.objects.latest("id")
        response = self.client.get(reverse("delete_review", args=[self.product.slug, self.review.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, reverse("product_detail", args=[self.product.slug])
        )