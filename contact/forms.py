from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Form for Customer messages
    """

    class Meta:
        """
        Define model, form fields and widgets
        """

        model = Contact
        fields = [
            "contact_reason",
            "name",
            "email",
            "subject",
            "message",
        ]

        labels = {
            "contact_reason": "Reason for Contact",
        }

        widgets = {"message": SummernoteWidget()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """
        Initializes the form attributes
        """
        placeholders = {
            "name": "Enter Full Name",
            "email": "Enter Email Address",
            "subject": "Enter Message Subject",
        }
        excluded_fields = ["contact_reason", "message"]

        for field_name, field in self.fields.items():
            if field_name not in excluded_fields:
                field.widget.attrs["placeholder"] = placeholders.get(
                    field_name, ""
                )
        self.fields["name"].widget.attrs["autofocus"] = True
