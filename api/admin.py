from django.contrib import admin
from api.models import CustomUser


@admin.register(CustomUser)
class UserModel(admin.ModelAdmin):
    list_display = ['username', 'is_staff']
