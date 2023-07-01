from django.test import TestCase, Client
from django.utils.text import slugify
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Blog, Comment


class TestBlogsViews(TestCase):
    """
    Testing Blogs View
    """

    def setUp(self):
        """
        Setup creates user, blog and logs user in
        """
        self.client = Client()
        self.user = User.objects.create_user(
            username="sean", email="finn@test.com", password="password"
        )
        self.user1 = User.objects.create_user(
            username="john", email="flynn@test.com", password="password"
        )
        self.superuser = User.objects.create_user(
            username="supersean",
            email="superfinn@test.com",
            password="superpassword",
            is_superuser=True,
        )
        self.blog = Blog.objects.create(
            author=self.user,
            title="Blog about testing",
            content="I like testing",
        )
        self.blog.likes.add(self.user)
        self.comment = Comment.objects.create(
            blog=self.blog, name=self.user, comment="I like ths blog post"
        )

    def test_blogs_page_renders(self):
        """
        Test that blogs view renders correct page
        """
        response = self.client.get(reverse("blogs"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/blogs.html")

    def test_blogs_detail_page_renders(self):
        """
        Test that blogs_detail view renders correct page
        """
        self.client.login(username="sean", password="password")
        response = self.client.get(
            reverse("blog_detail", args=[self.blog.slug])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/blog_detail.html")
        self.assertTrue(response.context["liked"])

    def test_like_blog(self):
        """
        Test liking/unliking of a blog post
        """
        self.client.login(username="sean", password="password")
        response = self.client.post(
            reverse("like_blog", args=[self.blog.slug])
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response.url, reverse("blog_detail", args=[self.blog.slug])
        )

        updated_blog = get_object_or_404(Blog, slug=self.blog.slug)
        self.assertFalse(updated_blog.likes.filter(id=self.user.id).exists())

        response = self.client.post(
            reverse("like_blog", args=[self.blog.slug])
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response.url, reverse("blog_detail", args=[self.blog.slug])
        )

        updated_blog = get_object_or_404(Blog, slug=self.blog.slug)
        self.assertTrue(updated_blog.likes.filter(id=self.user.id).exists())

    def test_like_blog_not_logged_in(self):
        """
        Test liking/unliking of a blog post not logged in
        """
        response = self.client.post(
            reverse("like_blog", args=[self.blog.slug])
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response.url, reverse("blog_detail", args=[self.blog.slug])
        )

    def test_add_blog(self):
        """
        Test adding a blog post
        """
        blog_count = Blog.objects.all().count()
        self.assertEqual(blog_count, 1)

        self.client.login(username="supersean", password="superpassword")
        response = self.client.get(reverse("add_blog"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/add_blog.html")

        blog_data = {
            "author": self.superuser,
            "title": "New Blog",
            "content": "New Blog Content",
        }

        response = self.client.post(
            reverse("add_blog"),
            data=blog_data,
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("blogs"))

        blog_count = Blog.objects.all().count()
        self.assertEqual(blog_count, 2)

    def test_add_blog_invalid(self):
        """
        Test adding a blog post with invalid data
        """
        blog_count = Blog.objects.all().count()
        self.assertEqual(blog_count, 1)

        self.client.login(username="supersean", password="superpassword")
        response = self.client.get(reverse("add_blog"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/add_blog.html")

        blog_data = {
            "author": self.superuser,
            "title": "",
            "content": "New Blog Content",
        }

        response = self.client.post(
            reverse("add_blog"),
            data=blog_data,
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/add_blog.html")

        blog_count = Blog.objects.all().count()
        self.assertEqual(blog_count, 1)

    def test_add_blog_no_superuser(self):
        """
        Test adding a blog post if not superuser
        """
        self.client.login(username="sean", password="password")
        response = self.client.get(reverse("add_blog"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("home"))

    def test_edit_blog(self):
        """
        Test edit a blog post
        """
        self.client.login(username="supersean", password="superpassword")
        response = self.client.get(reverse("edit_blog", args=[self.blog.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/edit_blog.html")

        self.assertEqual(self.blog.title, "Blog about testing")
        self.assertEqual(self.blog.content, "I like testing")

        blog_data = {
            "author": self.superuser,
            "title": "Update Blog",
            "content": "Updated Blog Content",
            "slug": "update-blog",
        }

        response = self.client.post(
            reverse("edit_blog", args=[self.blog.slug]),
            data=blog_data,
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, reverse("blog_detail", args=[blog_data["slug"]])
        )

        updated_blog = get_object_or_404(Blog, slug=blog_data["slug"])
        self.assertEqual(updated_blog.title, blog_data["title"])
        self.assertEqual(updated_blog.content, blog_data["content"])

    def test_edit_blog_invalid(self):
        """
        Test editing a blog post with invalid data
        """
        self.client.login(username="supersean", password="superpassword")
        response = self.client.get(reverse("edit_blog", args=[self.blog.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/edit_blog.html")

        blog_data = {
            "author": self.superuser,
            "title": "",
            "content": "Updated Blog Content",
            "slug": "update-blog",
        }

        response = self.client.post(
            reverse("edit_blog", args=[self.blog.slug]),
            data=blog_data,
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/edit_blog.html")

    def test_editing_blog_no_superuser(self):
        """
        Test editing a blog post if not superuser
        """
        self.client.login(username="sean", password="password")
        response = self.client.get(reverse("edit_blog", args=[self.blog.slug]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("home"))

    def test_delete_blog(self):
        """
        Test delete a blog post
        """
        blog_count = Blog.objects.all().count()
        self.assertEqual(blog_count, 1)
        self.client.login(username="supersean", password="superpassword")

        response = self.client.post(
            reverse("delete_blog", args=[self.blog.slug])
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("blogs"))

        blog_count = Blog.objects.all().count()
        self.assertEqual(blog_count, 0)

    def test_deleting_blog_no_superuser(self):
        """
        Test deleting a blog post if not superuser
        """
        self.client.login(username="sean", password="password")
        response = self.client.get(
            reverse("delete_blog", args=[self.blog.slug])
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("blogs"))

    def test_add_comment(self):
        """
        Test adding a comment to a blog post
        """
        comment_count = Comment.objects.all().count()
        self.assertEqual(comment_count, 1)

        self.client.login(username="sean", password="password")
        response = self.client.get(
            reverse("add_comment", args=[self.blog.slug])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/add_comment.html")

        comment_data = {
            "comment": "New Comment Content",
        }

        response = self.client.post(
            reverse("add_comment", args=[self.blog.slug]),
            data=comment_data,
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, reverse("blog_detail", args=[self.blog.slug])
        )

        comment_count = Comment.objects.all().count()
        self.assertEqual(comment_count, 2)

    def test_add_comment_invalid(self):
        """
        Test adding a comment to a blog post with invalid data
        """
        comment_count = Comment.objects.all().count()
        self.assertEqual(comment_count, 1)

        self.client.login(username="sean", password="password")
        response = self.client.get(
            reverse("add_comment", args=[self.blog.slug])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/add_comment.html")

        comment_data = {
            "comment": "",
        }

        response = self.client.post(
            reverse("add_comment", args=[self.blog.slug]),
            data=comment_data,
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/add_comment.html")

        comment_count = Comment.objects.all().count()
        self.assertEqual(comment_count, 1)

    def test_add_comment_not_logged_in(self):
        """
        Test adding a comment to a blog post not logged in
        """
        comment_count = Comment.objects.all().count()
        self.assertEqual(comment_count, 1)

        response = self.client.get(
            reverse("add_comment", args=[self.blog.slug])
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, reverse("blog_detail", args=[self.blog.slug])
        )

    def test_edit_comment(self):
        """
        Test edit a comment
        """
        self.client.login(username="sean", password="password")
        response = self.client.get(
            reverse("edit_comment", args=[self.blog.slug, self.comment.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/edit_comment.html")

        self.assertEqual(self.comment.comment, "I like ths blog post")

        comment_data = {
            "comment": "New Comment Content",
        }

        response = self.client.post(
            reverse("edit_comment", args=[self.blog.slug, self.comment.id]),
            data=comment_data,
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, reverse("blog_detail", args=[self.blog.slug])
        )

        updated_comment = get_object_or_404(Comment, id=self.comment.id)
        self.assertEqual(updated_comment.comment, comment_data["comment"])

    def test_edit_comment_invalid(self):
        """
        Test editing with invalid data
        """
        self.client.login(username="sean", password="password")
        response = self.client.get(
            reverse("edit_comment", args=[self.blog.slug, self.comment.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/edit_comment.html")

        self.assertEqual(self.comment.comment, "I like ths blog post")

        comment_data = {
            "comment": "",
        }

        response = self.client.post(
            reverse("edit_comment", args=[self.blog.slug, self.comment.id]),
            data=comment_data,
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/edit_comment.html")

    def test_edit_comment_not_comment_owner(self):
        """
        Test edit a comment not as the comment owner
        """
        comment_count = Comment.objects.all().count()
        self.assertEqual(comment_count, 1)

        self.client.login(username="sean", password="password")
        comment_data = {
            "comment": "New Comment Content",
        }
        response = self.client.post(
            reverse("add_comment", args=[self.blog.slug]),
            data=comment_data,
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, reverse("blog_detail", args=[self.blog.slug])
        )

        comment_count = Comment.objects.all().count()
        self.assertEqual(comment_count, 2)

        new_comment = Comment.objects.latest("id")
        self.assertEqual(new_comment.comment, comment_data["comment"])

        self.client.logout()

        self.client.login(username="john", password="password")

        comment = Comment.objects.latest("id")
        response = self.client.get(
            reverse("edit_comment", args=[self.blog.slug, comment.id])
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, reverse("blog_detail", args=[self.blog.slug])
        )

    def test_delete_comment(self):
        """
        Test delete a blog post comment
        """
        comment_count = Comment.objects.all().count()
        self.assertEqual(comment_count, 1)
        self.client.login(username="sean", password="password")

        response = self.client.post(
            reverse("delete_comment", args=[self.blog.slug, self.comment.id])
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, reverse("blog_detail", args=[self.blog.slug])
        )

        comment_count = Comment.objects.all().count()
        self.assertEqual(comment_count, 0)
        
    def test_delete_comment_not_comment_owner(self):
        """
        Test delete a blog post comment when not comment owner
        """
        comment_count = Comment.objects.all().count()
        self.assertEqual(comment_count, 1)

        self.client.login(username="sean", password="password")
        comment_data = {
            "comment": "New Comment Content",
        }
        response = self.client.post(
            reverse("add_comment", args=[self.blog.slug]),
            data=comment_data,
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, reverse("blog_detail", args=[self.blog.slug])
        )

        comment_count = Comment.objects.all().count()
        self.assertEqual(comment_count, 2)
        
        self.client.logout()

        self.client.login(username="john", password="password")

        comment = Comment.objects.latest("id")
        response = self.client.get(
            reverse("delete_comment", args=[self.blog.slug, comment.id])
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, reverse("blog_detail", args=[self.blog.slug]))