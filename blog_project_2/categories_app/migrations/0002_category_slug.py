# Generated by Django 5.0 on 2023-12-28 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
