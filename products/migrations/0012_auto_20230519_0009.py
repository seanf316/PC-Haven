# Generated by Django 3.2 on 2023-05-19 00:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_alter_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='sub_category',
        ),
        migrations.DeleteModel(
            name='SubCategory',
        ),
    ]