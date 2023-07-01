from django.test import TestCase
from .models import Contact


class TestContactModel(TestCase):
    """
    Testing Contact Model
    """

    def setUp(self):
        """
        Sets the Contact Object with required attributes
        """

        self.contact = Contact.objects.create(
            contact_reason="general_query",
            name="sean",
            email="Sean@test.com",
            subject="No Product",
            message="Cant find Product",
        )

        self.expected_str = str(f"Contact Message from {self.contact.name}")

    def test_contact_model(self):
        """
        Tests the Contact model's attributes
        """
        self.assertEqual(self.contact.contact_reason, "general_query")
        self.assertEqual(self.contact.name, "sean")
        self.assertEqual(self.contact.email, "Sean@test.com")
        self.assertEqual(self.contact.subject, "No Product")
        self.assertEqual(self.contact.message, "Cant find Product")
        self.assertEqual(str(self.contact), self.expected_str)
