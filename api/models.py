from django.db import models


# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.IntegerField()
    email = models.EmailField()

# class Seller(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     address = models.CharField(max_length=100)
#     city = models.CharField(max_length=100)
#     postal_code = models.IntegerField()
#     email = models.EmailField()