from django import forms
from products.widgets import CustomClearableFileInput
from django_summernote.widgets import SummernoteWidget
from .models import Blog, Comment


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
            "author",
            "image_url",
        ]

        widgets = {
            "content": SummernoteWidget(),
            "image": CustomClearableFileInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """
        Initializes the form attributes
        """
        placeholders = {
            "title": "Enter Blog Title",
        }
        for field_name, field in self.fields.items():
            field.widget.attrs["placeholder"] = placeholders.get(
                field_name, ""
            )
        self.fields["title"].widget.attrs["autofocus"] = True


class CommentForm(forms.ModelForm):
    """
    Form to Add/Edit/Delete Comment
    """

    class Meta:
        """
        Define model, form fields and widgets
        """

        model = Comment
        fields = ("comment",)

        labels = {
            "comment": "Comment (Max 300 Characters) ",
        }

        widgets = {
            "comment": SummernoteWidget(),
        }
