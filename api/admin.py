from django.contrib import admin
from api.models import Customer
# Register your models here.
@admin.register(Customer)
class CustomerModel (admin.ModelAdmin):
    list_display = ['id','first_name', 'last_name', 'address', 'city', 'postal_code', 'email']