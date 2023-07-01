from django.test import TestCase
from django.contrib.auth.models import User
from .models import Blog, Comment


class TestBlogModel(TestCase):
    """
    Testing Blog Model
    """

    def setUp(self):
        """
        Sets the Blog Object with required attributes
        """
        self.user = User.objects.create_user(
            username="sean", email="finn@test.com", password="password"
        )

        self.blog = Blog.objects.create(
            author=self.user,
            title="Blog about testing",
            content="I like testing",
        )

        self.expected_str = str(f"Blog Post - {self.blog.title}")

    def test_blog_model(self):
        """
        Tests the Review model's attributes
        """
        self.assertEqual(self.blog.author.username, "sean")
        self.assertEqual(self.blog.title, "Blog about testing")
        self.assertEqual(self.blog.content, "I like testing")
        self.assertEqual(str(self.blog), self.expected_str)


class TestCommentModel(TestCase):
    """
    Testing Comment Model
    """

    def setUp(self):
        """
        Sets the Comment Object with required attributes
        """
        self.user = User.objects.create_user(
            username="sean", email="finn@test.com", password="password"
        )

        self.blog = Blog.objects.create(
            author=self.user,
            title="Blog about testing",
            content="I like testing",
        )

        self.comment = Comment.objects.create(
            blog=self.blog,
            name=self.user,
            comment="I like this blog",
        )

        self.expected_str = str(f"Comment by {self.comment.name}")

    def test_comment_model(self):
        """
        Tests the Comment model's attributes
        """
        self.assertEqual(self.comment.name.username, "sean")
        self.assertEqual(self.comment.blog, self.blog)
        self.assertEqual(self.comment.comment, "I like this blog")
        self.assertEqual(str(self.comment), self.expected_str)
