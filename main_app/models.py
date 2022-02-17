from django.db import models
from django.urls import reverse

# Create your models here.

class Wallet(models.Model):
    name = models.CharField(max_length=100)
    designer = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('wallets_detail', kwargs={'wallet_id': self.id})

class Purse(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('purses_detail', kwargs={'purse_id': self.id})

