# Generated by Django 3.0.1 on 2019-12-26 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film_app', '0005_auto_20191225_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='about',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='film',
            name='image',
            field=models.ImageField(blank=True, default='posters/no_cover.jpg', upload_to='posters/'),
        ),
    ]
