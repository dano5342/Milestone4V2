from django.db import models
from annoying.fields import AutoOneToOneField
from django.contrib.auth.models import User


class Category(models.Model):
    category = models.CharField(max_length=40)

    def __str__(self):
        return self.category

class Product(models.Model):
    title = models.CharField(max_length=40)
    summary = models.CharField(max_length=120)
    description = models.TextField(max_length=500, blank=False)
    sold_by = AutoOneToOneField(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default="")

    def __str__(self):
        return self.title
