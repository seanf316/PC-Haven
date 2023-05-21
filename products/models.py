from django.db import models
from django_resized import ResizedImageField
from django.core.validators import MinValueValidator
from django.utils.text import slugify
import string
import random


class CategoryGroup(models.Model):
    """A model for the Category Group of the Product"""

    name = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    sub_categories = models.ManyToManyField("SubCategory")

    class Meta:
        """ "
        Alters the name of the Category Group in the admin panel
        """

        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class SubCategory(models.Model):
    """A model for the Sub Category of the Product"""

    name = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        """ "
        Alters the name of the Sub Category in the admin panel
        """

        verbose_name_plural = "Sub Categories"

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """A model for the the Products"""

    category = models.ForeignKey(
        "CategoryGroup", null=True, blank=True, on_delete=models.SET_NULL
    )
    sub_category = models.ForeignKey(
        "SubCategory", null=True, blank=True, on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=254, null=True, blank=True, unique=True)
    name = models.CharField(max_length=254)
    slug = models.SlugField(
        max_length=254, null=True, blank=True, unique=True, editable=False
    )
    description = models.TextField()
    information = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = ResizedImageField(
        size=[600, 450],
        quality=75,
        upload_to="products",
        force_format="WEBP",
        blank=True,
        null=True,
    )
    stock_level = models.IntegerField(
        default=1, validators=[MinValueValidator(0)]
    )
    in_stock = models.BooleanField(default=True)
    created_on = models.DateTimeField(
        auto_now_add=True,
        null=True,
    )

    class Meta:
        """ "
        Alters the order of the Products in the admin panel
        """

        ordering = ("name",)

    def __str__(self):
        return self.name

    def generate_sku(self, length=8):
        prefix = "pp"
        chars = string.ascii_uppercase + string.digits
        unique_id = "".join(random.choice(chars) for _ in range(length))
        sku = f"{prefix}-{unique_id}"
        return sku

    def save(self, *args, **kwargs):
        if self.stock_level <= 0:
            self.in_stock = False
        else:
            self.in_stock = True
        if not self.sku:
            self.sku = self.generate_sku()
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
