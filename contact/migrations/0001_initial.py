# Generated by Django 3.2 on 2023-06-09 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_received', models.DateTimeField(auto_now_add=True)),
                ('contact_reason', models.CharField(choices=[('general_query', 'General Query'), ('product_query', 'Product Query'), ('technical_issue', 'Technical Issue'), ('other', 'Other')], default='general_query', max_length=100)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.TextField()),
                ('pending_reply', models.BooleanField(default=True)),
                ('marked_as_done', models.BooleanField(default=False)),
            ],
        ),
    ]
