# Generated by Django 3.2 on 2023-06-11 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_alter_product_stock_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='featured_product',
            field=models.BooleanField(default=False),
        ),
    ]
