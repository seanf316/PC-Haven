# Generated by Django 3.2 on 2023-05-14 20:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_product_stock_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock_level',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
