from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from products.models import Product


class Review(models.Model):
    """
    Model for creating a Review
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_on = models.DateTimeField(
        auto_now_add=True,
        null=True,
    )
    review = models.TextField()
    rating = models.IntegerField(
        default=1, validators=[MaxValueValidator(5), MinValueValidator(1)]
    )

    class Meta:
        """
        Order set to the created on attribute
        """

        ordering = ["-created_on"]

    def __str__(self):
        """
        Returns the User username and the product name as a string
        representation of the object.
        """
        return f"{self.user.username} - {self.product.name}"
