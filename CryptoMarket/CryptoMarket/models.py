# models.py
from django.db import models

class DogecoinPrice(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    price = models.FloatField()

class Meta:
    app_label = 'CryptoMarket'
