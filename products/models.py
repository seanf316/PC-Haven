from django.db import models
from djrichtextfield.models import RichTextField
from django.utils.text import slugify

class CategoryGroup(models.Model):
    """ A model for the Category Group of the Product """
    
    verbose_name_plural = 'Categories'
    
    name = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name
    

class SubCategory(models.Model):
    """ A model for the Sub Category of the Product """
    
    verbose_name_plural = 'Sub Categories'
    name = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name

class Product(models.Model):
    """ A model for the the Products """
    
    category = models.ForeignKey(
        "CategoryGroup", null=True, blank=True, on_delete=models.SET_NULL
    )
    sub_categeory = models.ForeignKey(
        "SubCategory", null=True, blank=True, on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=254, unique=True)
    name = models.CharField(max_length=254)
    slug = models.SlugField(
        max_length=254, null=True,
        blank=True, unique=True,
        editable=False)
    description = RichTextField()
    information = RichTextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    def generate_sku(self, length=8):
        prefix = "pp"
        chars = string.ascii_uppercase + string.digits
        unique_id = ''.join(random.choice(chars) for _ in range(length))
        sku = f"{prefix}-{unique_id}"
        return sku

    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = self.generate_sku()
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)