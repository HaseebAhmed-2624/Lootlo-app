from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class UserType(models.Model):
    CHOICES = (
        ('buyer', 'Buyer'),
        ('seller', 'Seller'),
        ('admin', 'Admin'),
    )

    user_type = models.CharField(max_length=20, choices=CHOICES, default='buyer')


class CustomUser(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='custom_user_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set', blank=True)
    address = models.CharField(max_length=100, default='', blank=True)
    city = models.CharField(max_length=100, default='', blank=True)
    postal_code = models.IntegerField(default='0', blank=True)
    user_type = models.OneToOneField(UserType, on_delete=models.CASCADE, default=None, blank=True,
                                     related_name='usertype')

    def __str__(self):
        return self.username
