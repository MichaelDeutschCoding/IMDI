from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import date


class Country(models.Model):
    name = models.CharField(max_length=63,unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=63, unique=True)

    def __str__(self):
        return f"{self.name}"


class Director(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Film(models.Model):
    title = models.CharField(max_length=63)
    release_date = models.DateField(default=date.today)
    country = models.ForeignKey(Country, null=True, on_delete=models.SET_NULL)
    category = models.ManyToManyField(Category)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    rating = models.IntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(10)])
    image = models.ImageField(upload_to='posters/', default='posters/no_cover.jpg', blank=True)
    about = models.TextField(default='', blank=True)

    def __str__(self):
        return self.title
