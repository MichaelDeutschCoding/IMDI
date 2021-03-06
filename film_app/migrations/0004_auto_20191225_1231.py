# Generated by Django 3.0.1 on 2019-12-25 12:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film_app', '0003_auto_20191225_0820'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='about',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='film',
            name='image',
            field=models.ImageField(null=True, upload_to='film_app/images'),
        ),
        migrations.AlterField(
            model_name='film',
            name='rating',
            field=models.IntegerField(default=5, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
    ]
