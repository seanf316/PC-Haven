from django.db import models
from django_resized import ResizedImageField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
import string
import random


class CategoryGroup(models.Model):
    """A model for the Category Group of the Product"""

    name = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    sub_categories = models.ManyToManyField("SubCategory")

    class Meta:
        """
        Alters the name of the Category Group in the admin panel
        """

        verbose_name_plural = "Categories"

    def __str__(self):
        """
        Returns the name of the Category as a string representation of the object.
        """
        return self.name

    def get_friendly_name(self):
        """
        Passes the friendly name to the template/admin panel
        """
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
        """
        Returns the name of the Sub-Category as a string representation of the object.
        """
        return self.name

    def get_friendly_name(self):
        """
        Passes the friendly name to the template/admin panel
        """
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
    features = models.TextField()
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = ResizedImageField(
        size=[600, None],
        quality=75,
        upload_to="products",
        force_format="WEBP",
        blank=True,
        null=True,
    )
    stock_level = models.IntegerField(
        default=1, validators=[MinValueValidator(0), MaxValueValidator(1000)]
    )
    in_stock = models.BooleanField(default=True)
    created_on = models.DateTimeField(
        auto_now_add=True,
        null=True,
    )
    featured_product = models.BooleanField(default=False)
    has_sale = models.BooleanField(default=False)
    discount = models.IntegerField(
        default=10,
        help_text="Discount in Percentage",
        verbose_name="Discount If Product On Sale",
    )
    sale_price = models.DecimalField(
        max_digits=6, decimal_places=2, default=0.00
    )

    class Meta:
        """ "
        Alters the order of the Products in the admin panel
        """

        ordering = ("name",)

    def __str__(self):
        """
        Returns the name of the Product as a string representation of the object.
        """
        return self.name

    def generate_sku(self, length=8):
        """
        Generates a sku number for each Product
        """
        prefix = "pp"
        chars = string.ascii_uppercase + string.digits
        unique_id = "".join(random.choice(chars) for _ in range(length))
        sku = f"{prefix}-{unique_id}"
        return sku

    def save(self, *args, **kwargs):
        """
        Override the original save method and updates the stock level
        """
        if self.stock_level <= 0:
            self.in_stock = False
        else:
            self.in_stock = True
        if self.has_sale:
            self.sale_price = self.price - (self.price * (self.discount) / 100)
        else:
            self.sale_price = self.price
        if not self.sku:
            self.sku = self.generate_sku()
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
