from django.db import models
from django.contrib.auth.models import User

"""Inheriting abstract base user class in other models"""

# Create your models here.
class BasicUser(models.Model):
    first_name = models.CharField(max_length=100,default=None,blank=True)
    last_name = models.CharField(max_length=100,default=None,blank=True)
    address = models.CharField(max_length=100,default=None,blank=True)
    city = models.CharField(max_length=100,default=None,blank=True)
    postal_code = models.IntegerField(default=None,blank=True)
    email = models.EmailField(max_length=70,unique=True)

    class Meta:
        abstract = True


class Customer(BasicUser):
    customer_user = models.OneToOneField(User, related_name='customer_user', on_delete=models.DO_NOTHING, default=1)


class Seller(BasicUser):
    seller_user = models.OneToOneField(User, related_name='seller_user', on_delete=models.DO_NOTHING, default=1)


class Admin(BasicUser):
    admin_user = models.OneToOneField(User, related_name='admin_user', on_delete=models.DO_NOTHING, default=1)