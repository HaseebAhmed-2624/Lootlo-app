from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class UserType(models.Model):
    id = models.IntegerField(primary_key=True)
    usertype = models.CharField(max_length=20)


class CustomUser(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='custom_user_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set', blank=True)
    address = models.CharField(max_length=150, default='', blank=True)
    city = models.CharField(max_length=150, default='', blank=True)
    postal_code = models.IntegerField(default='0', blank=True)
    user_type = models.ForeignKey(UserType, related_name='user_type', on_delete=models.DO_NOTHING, default=1)

    def __str__(self):
        return self.username
