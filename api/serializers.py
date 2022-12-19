from rest_framework import serializers
from api.models import Customer
from rest_framework.permissions import AllowAny

# Create your serializers here

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'address', 'city', 'postal_code', 'email']
