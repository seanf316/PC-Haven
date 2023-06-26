from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class UserForm(forms.ModelForm):
    """
    Form to Edit User-Username/Email
    """

    class Meta:
        """
        Define model, form fields
        """

        model = User
        fields = ["email", "first_name", "last_name"]

    def __init__(self, *args, **kwargs):
        """
        Add placeholders
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            "email": "Email",
            "first_name": "First name",
            "last_name": "Surname",
        }
        for field_name, field in self.fields.items():
            field.widget.attrs["placeholder"] = placeholders.get(
                field_name, ""
            )


class UserProfileForm(forms.ModelForm):
    class Meta:
        """
        Define model, form fields
        """

        model = UserProfile
        exclude = ("user",)

        labels = {
            "default_phone_number": "Phone Number",
            "default_postcode": "Eircode/Postcode",
            "default_street_address1": "Street Address 1",
            "default_street_address2": "Street Address 2",
            "default_town_or_city": "Town or City",
            "default_county": "County, State or Locality",
            "default_country": "Country",
        }

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            "default_phone_number": "Phone Number",
            "default_postcode": "Eircode/Postcode",
            "default_street_address1": "Street Address 1",
            "default_street_address2": "Street Address 2",
            "default_town_or_city": "Town or City",
            "default_county": "County, State or Locality",
        }
        for field in self.fields:
            if field != "default_country":
                if self.fields[field].required:
                    placeholder = f"{placeholders[field]} *"
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs["placeholder"] = placeholder
