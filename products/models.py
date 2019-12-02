from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    category = models.CharField(max_length=40)
    image = models.ImageField(upload_to='images', null=True)
    description = models.TextField(max_length=1000, null=True)

    def __str__(self):
        return self.category


class Product(models.Model):
    title = models.CharField(max_length=120)
    summary = models.CharField(max_length=240)
    description = models.TextField(max_length=1000, blank=False)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 default="")
    image = models.ImageField(upload_to="images", null=True)
    pubd = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
