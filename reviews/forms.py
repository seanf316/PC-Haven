from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    Form to Edit/Delete Review
    """

    class Meta:
        """
        Define model, form fields and widgets
        """

        model = Review
        fields = [
            "review",
            "rating",
        ]
        labels = {
            "review": "Review",
            "rating": "Rating (1-5)",
        }

        widgets = {"review": SummernoteWidget()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """
        Initializes the form attributes
        """
        self.fields["rating"].widget.attrs["min"] = 1
        self.fields["rating"].widget.attrs["max"] = 5
        self.fields["review"].widget.attrs["autofocus"] = True
