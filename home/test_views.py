from django.test import TestCase
from django.urls import reverse


class TestHomeViews(TestCase):
    """
    Testing Home View
    """

    def test_home_page_renders(self):
        """
        Test that home view renders correct page
        """
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/index.html")

    def test_privacy_page_renders(self):
        """
        Test that privacy view renders correct page
        """
        response = self.client.get(reverse("privacy"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/privacy_policy.html")

    def test_terms_page_renders(self):
        """
        Test that terms and conditions view renders correct page
        """
        response = self.client.get(reverse("terms"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/terms.html")

    def test_faq_page_renders(self):
        """
        Test that FAQ view renders correct page
        """
        response = self.client.get(reverse("faq"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/faq.html")
