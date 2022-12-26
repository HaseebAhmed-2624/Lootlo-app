from django.contrib import admin
from api.models import CustomUser


# # Register your models here.
# @admin.register(Seller)
# class SellerModel(admin.ModelAdmin):
#     list_display = ['id', 'first_name', 'last_name', 'address', 'city', 'postal_code', 'email', 'seller_user']
#
#
# @admin.register(Customer)
# class CustomerModel(admin.ModelAdmin):
#     list_display = ['id', 'first_name', 'last_name', 'address', 'city', 'postal_code', 'email', 'customer_user']
#
#
# @admin.register(Admin)
# class AdminModel(admin.ModelAdmin):
#     list_display = ['id', 'first_name', 'last_name', 'address', 'city', 'postal_code', 'email', 'admin_user']
@admin.register(CustomUser)
class UserModel(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'address', 'city', 'postal_code', 'email', 'password']

