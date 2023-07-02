from django.test import TestCase, Client
from django.urls import reverse
from .forms import ContactForm


class TestContactViews(TestCase):
    """
    Testing Contact View
    """

    def test_contact_page_renders(self):
        """
        Test that contact view renders correct page
        """
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contact/contact.html")

    def test_contact_message(self):
        """
        Test that contact message works
        """
        contact_data = {
            "contact_reason": "general_query",
            "name": "Sean",
            "email": "Sean@test.com",
            "subject": "No Product",
            "message": "Cant find Product",
        }
        response = self.client.post(reverse("contact"), data=contact_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("home"))

    def test_contact_message_invalid_data(self):
        """
        Test that contact message wont work with invalid data
        """
        contact_data = {
            "contact_reason": "",
            "name": "Sean",
            "email": "Sean@test.com",
            "subject": "No Product",
            "message": "Cant find Product",
        }
        response = self.client.post(reverse("contact"), data=contact_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contact/contact.html")
