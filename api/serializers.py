from rest_framework import serializers
from api.models import CustomUser
from rest_framework.permissions import AllowAny


# Create your serializers he                                                        re
#
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ['first_name', 'last_name', 'address', 'city', 'postal_code', 'email']
#
#
# class SellerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Seller
#         fields = '__all__'
#
#
# class AdminSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Admin
#         fields = '__all__'
