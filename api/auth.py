# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework_simplejwt.views import TokenObtainPairView
# # from django.contrib.auth.models import User
#
# class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)
#
#         # Add custom claims
#         token['name'] = user.username
#         # ...
#         return token
#
#
# class CustomTokenObtainPairView(TokenObtainPairView):
#     serializer_class = CustomTokenObtainPairSerializer



# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
#     """Customizes JWT default Serializer to add more information about user"""
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)
#         token['name'] = user.name
#         token['email'] = user.email
#         token['is_superuser'] = user.is_superuser
#         token['is_staff'] = user.is_staff
#
#         return token