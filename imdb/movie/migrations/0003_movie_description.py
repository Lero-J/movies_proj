# Generated by Django 4.2.15 on 2024-09-15 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_remove_movie_category_movie_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
