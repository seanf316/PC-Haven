from django.test import TestCase
from .forms import ContactForm


class TestContactForm(TestCase):
    """Testing Contact Form"""

    def test_contactform_valid(self):
        """Test Contact form is valid"""
        form = ContactForm(
            {
                "contact_reason": "general_query",
                "name": "Sean",
                "email": "Sean@test.com",
                "subject": "No Product",
                "message": "Cant find Product",
            }
        )
        self.assertTrue(form.is_valid())

    def test_contactform_not_valid(self):
        """Test Contact form is not valid"""
        form = ContactForm(
            {
                "contact_reason": "general_query",
                "name": "",
                "email": "Sean@test.com",
                "subject": "No Product",
                "message": "Cant find Product",
            }
        )
        self.assertIn("name", form.errors.keys())
        self.assertEqual(form.errors["name"][0], "This field is required.")
        self.assertFalse(form.is_valid())

    def test_contactform_name_above_max_characters(self):
        """Contact name field exceeds 50 characters"""
        form = ContactForm(
            {
                "contact_reason": "general_query",
                "name": str("a" * 51),
                "email": "Sean@test.com",
                "subject": "No Product",
                "message": "Cant find Product",
            }
        )
        self.assertIn("name", form.errors.keys())
        self.assertEqual(
            form.errors["name"][0],
            "Ensure this value has at most 50 characters (it has 51).",
        )
        self.assertFalse(form.is_valid())

    def test_contactform_subject_above_max_characters(self):
        """Contact subject field exceeds 50 characters"""
        form = ContactForm(
            {
                "contact_reason": "general_query",
                "name": str("a" * 40),
                "email": "Sean@test.com",
                "subject": str("a" * 51),
                "message": "Cant find Product",
            }
        )
        self.assertIn("subject", form.errors.keys())
        self.assertEqual(
            form.errors["subject"][0],
            "Ensure this value has at most 50 characters (it has 51).",
        )
        self.assertFalse(form.is_valid())
