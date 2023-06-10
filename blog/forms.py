from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Blog


class BlogForm(forms.ModelForm):
    """
    Form to Create/Edit Blog
    """

    class Meta:
        """
        Define model, form fields and widgets
        """

        model = Blog
        fields = "__all__"
        exclude = [
            "created_on",
            "likes",
        ]
        labels = {
            "review": "Review",
            "rating": "Rating (1-5)",
        }

        widgets = {"content": SummernoteWidget()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """
        Initializes the form attributes
        """
        placeholders = {
            "title": "Enter Blog Title",
        }
        self.fields["title"].widget.attrs["autofocus"] = True
