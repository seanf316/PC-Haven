# Generated by Django 3.2 on 2023-06-15 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_comment_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=254, null=True, unique=True),
        ),
    ]
