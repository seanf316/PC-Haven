from django.test import TestCase
from .forms import BlogForm, CommentForm


class TestBlogForm(TestCase):
    """Testing Blog Form"""

    def test_blogform_valid(self):
        """Test Blog form is valid"""
        form = BlogForm(
            {
                "title": "This is a good blog",
                "content": "This is blog content",
            }
        )
        self.assertTrue(form.is_valid())

    def test_blogform_not_valid(self):
        """Test Blog form is not valid"""
        form = BlogForm(
            {
                "title": "",
                "content": "This is blog content",
            }
        )
        self.assertIn("title", form.errors.keys())
        self.assertEqual(form.errors["title"][0], "This field is required.")
        self.assertFalse(form.is_valid())

    def test_blogform_title_above_max_characters(self):
        """Blog form title field exceeds 50 characters"""
        form = BlogForm(
            {
                "title": str("a" * 51),
                "content": "This is blog content",
            }
        )
        self.assertIn("title", form.errors.keys())
        self.assertEqual(
            form.errors["title"][0],
            "Ensure this value has at most 50 characters (it has 51).",
        )
        self.assertFalse(form.is_valid())


class TestCommentForm(TestCase):
    """Testing Comment Form"""

    def test_commentform_valid(self):
        """Test comment form is valid"""
        form = CommentForm({"comment": "This is a good blog ppost"})
        self.assertTrue(form.is_valid())

    def test_commentform_not_valid(self):
        """Comment form is not valid"""
        form = CommentForm({"comment": ""})
        self.assertIn("comment", form.errors.keys())
        self.assertEqual(form.errors["comment"][0], "This field is required.")
        self.assertFalse(form.is_valid())

    def test_commentform_comment_above_max_characters(self):
        """Comment form comment field exceeds 300 characters"""
        form = CommentForm({"comment": str("a" * 301)})
        self.assertIn("comment", form.errors.keys())
        self.assertEqual(
            form.errors["comment"][0],
            "Ensure this value has at most 300 characters (it has 301).",
        )
        self.assertFalse(form.is_valid())
