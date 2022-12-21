from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission


class CustomUser(AbstractUser):
    postal_code = models.IntegerField()
    groups = models.ManyToManyField(Group, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set')

class UserType(models.Model):
    isCustomer=models.CharField(max_length=10)
    isSeller=models.CharField(max_length=10)
    isAdmin=models.CharField(max_length=10)
