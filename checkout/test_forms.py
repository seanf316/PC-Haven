from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import UserProfile
from .forms import OrderForm


class TestOrderForm(TestCase):
    """Testing Order Form"""
        
    def test_orderform_valid(self):
        """Test Order form is valid"""
        form = OrderForm(
            {
                "full_name": "Sean Finn",
                "email": "finn@test.com",
                "phone_number": "123456789",
                "street_address1": "1 test house",
                "street_address2": "1 test street",
                "town_or_city": "test city",
                "county": "test county",
                "postcode": "v12 y934",
                "country": "IE",
            }
        )
        self.assertTrue(form.is_valid())

    def test_orderform_not_valid(self):
        """Test Order form is not valid"""
        form = OrderForm(
            {
                "full_name": "",
                "email": "finn@test.com",
                "phone_number": "123456789",
                "street_address1": "1 test house",
                "street_address2": "1 test street",
                "town_or_city": "test city",
                "county": "test county",
                "postcode": "v12 y934",
                "country": "IE",
            }
        )
        self.assertIn("full_name", form.errors.keys())
        self.assertEqual(form.errors["full_name"][0], "This field is required.")
        self.assertFalse(form.is_valid())

    def test_orderform_name_above_max_characters(self):
        """Oder form full_name field exceeds 50 characters"""
        form = OrderForm(
            {
                "full_name": str("a"*51),
                "email": "finn@test.com",
                "phone_number": "123456789",
                "street_address1": "1 test house",
                "street_address2": "1 test street",
                "town_or_city": "test city",
                "county": "test county",
                "postcode": "v12 y934",
                "country": "IE",
            }
        )
        self.assertIn("full_name", form.errors.keys())
        self.assertEqual(
            form.errors["full_name"][0],
            "Ensure this value has at most 50 characters (it has 51).",
        )
        self.assertFalse(form.is_valid())

