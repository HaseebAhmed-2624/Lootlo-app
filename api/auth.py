from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Customizes JWT default Serializer to add more information about user"""
    default_error_messages = {
        "no_active_account": "Invalid username or password"
    }

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token["user_reference"] = {"first_name": user.first_name, "last_name": user.last_name,
                                   "email": user.email,
                                   "user_type": user.user_type.id}
        return token


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


