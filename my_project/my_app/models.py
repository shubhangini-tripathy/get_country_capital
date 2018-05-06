from django.db import models

# Create your models here.
class CountryDetail(models.Model):
    country = models.CharField(max_length=150,primary_key = True)
    capital = models.CharField(max_length=150)
