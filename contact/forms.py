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
            "sunject": "Enter Message Subject",
        }
        self.fields["subject"].widget.attrs["autofocus"] = True
