from django.test import TestCase
from .forms import ReviewForm


class TestReviewForm(TestCase):
    """Testing Review Form"""
    def test_reviewform_valid(self):
        """Test Review form is valid"""
        form = ReviewForm(
            {
                "review": "This is a good product",
                "rating": 5,
            }
        )
        self.assertTrue(form.is_valid())

    def test_reviewform_invalid(self):
        """Test Review form is invalid"""
        form = ReviewForm(
            {
                "review": "",
                "rating": 5,
            }
        )
        self.assertIn("review", form.errors.keys())
        self.assertEqual(form.errors["review"][0], "This field is required.")
        self.assertFalse(form.is_valid())

    def test_reviewform_rating_below_min(self):
        """Review form has rating below 1"""
        form = ReviewForm(
            {
                "review": "Good",
                "rating": 0,
            }
        )
        self.assertIn("rating", form.errors.keys())
        self.assertEqual(
            form.errors["rating"][0],
            "Ensure this value is greater than or equal to 1.",
        )
        self.assertFalse(form.is_valid())

    def test_reviewform_rating_above_max(self):
        """Review form has rating above 5"""
        form = ReviewForm(
            {
                "review": "Good",
                "rating": 6,
            }
        )
        self.assertIn("rating", form.errors.keys())
        self.assertEqual(
            form.errors["rating"][0],
            "Ensure this value is less than or equal to 5.",
        )
        self.assertFalse(form.is_valid())
