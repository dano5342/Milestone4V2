from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'


class UserAddress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default="")
    address1 = models.CharField(max_length=128)
    address2 = models.CharField(max_length=128, blank=False)
    city_or_town = models.CharField(max_length=128)
    county = models.CharField(max_length=128, blank=False)
    country = models.CharField(max_length=128)
    zip_or_postcode = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.user.username} Address'