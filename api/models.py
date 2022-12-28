# models
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class UserType(models.Model):
    number = models.IntegerField()
    usertype = models.CharField(max_length=20)


class CustomUser(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='custom_user_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set', blank=True)
    address = models.CharField(max_length=100, default='', blank=True)
    city = models.CharField(max_length=100, default='', blank=True)
    postal_code = models.IntegerField(default='0', blank=True)
    user_type = models.ManyToManyField(UserType, related_name='user_type')

    def __str__(self):
        return self.username

    # def save(self, *args, **kwargs):
    #     try:
    #         UserType.objects.create(user_id=self.id)
    #         super().save(*args, **kwargs)  #
    #     except Exception as e:
    #         print('User Type exception ', e)
