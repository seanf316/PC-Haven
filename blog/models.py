from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField


class Blog(models.Model):
    """A model for Blog Posts"""

    image = ResizedImageField(
        size=[1000, None],
        quality=75,
        upload_to="blog",
        force_format="WEBP",
        blank=True,
        null=True,
    )
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    title = models.CharField(null=False, blank=False, max_length=50)
    content = models.TextField(
        null=False,
        blank=False,
    )
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(
        User, related_name="blogpost_like", blank=True
    )

    class Meta:
        """
        Order set to the created_on attribute
        """

        ordering = ["-created_on"]

    def __str__(self):
        """
        Returns the name of the Blog as a string representation of the object.
        """
        return f"Blog Post - {self.title}"

    def number_of_likes(self):
        """
        Returns the Blog likes count
        """
        return self.likes.count()
