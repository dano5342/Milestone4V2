from django.db import models
from products.models import Product


class Order(models.Model):
    full_name = models.CharField(max_length=64, blank=False)
    phone_number = models.CharField(max_length=25, blank=False)
    country = models.CharField(max_length=64, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    city_or_town = models.CharField(max_length=128, blank=False)
    address2 = models.CharField(max_length=128, blank=False)
    address1 = models.CharField(max_length=128, blank=False)
    county = models.CharField(max_length=128, blank=False)
    date = models.DateField()

    def __str__(self):
        return '{0}-{1}-{2}'.format(self.id, self.date, self.full_name)


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return '{0} {1} @ {2}'.format(self.quantity,
                                      self.product.title, self.product.price)
