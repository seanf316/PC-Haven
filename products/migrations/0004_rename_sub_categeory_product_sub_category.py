# Generated by Django 3.2 on 2023-05-11 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='sub_categeory',
            new_name='sub_category',
        ),
    ]
