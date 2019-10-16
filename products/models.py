from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=40)
    summary = models.CharField(max_length=120)
    description = models.TextField(max_length=500, blank=False)
    sold_by = models.OneToOneField(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.title
