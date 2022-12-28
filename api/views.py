from rest_framework import viewsets
from django.contrib.auth import get_user_model
from api.serializers import UserSerializer
from rest_framework import permissions
from api.permissions import IsOwnerPermission
from django.core.signals import request_started
from django.dispatch import receiver
from api.models import UserType
from rest_framework_simplejwt.authentication import JWTAuthentication


@receiver(request_started)
def first_request_received(sender, **kwargs):

    """Checks if UserType records exists if not then creates records"""

    check_usertype = UserType.objects.all()
    if not check_usertype:
        print("User Type is empty")
        UserType.objects.create(id=1, usertype="buyer")
        UserType.objects.create(id=2, usertype="seller")
        UserType.objects.create(id=3, usertype="admin")


class UserModelViewSet(viewsets.ModelViewSet):
    User = get_user_model()
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]

    def get_authenticators(self):

        """Remove JWT Authentication from User Creation"""

        if self.request.method == 'POST':
            self.authentication_classes = []
        else:
            self.authentication_classes = [JWTAuthentication]
        # Use the SessionAuthentication class for all other request methods
        return []

    def get_permissions(self):

        """Assigning permissions for actions in ModelViewSet"""

        if self.action == 'retrieve':
            permission_classes = [permissions.IsAdminUser]
        elif self.action == 'list':
            permission_classes = [permissions.IsAdminUser]
        elif self.action == 'update':
            permission_classes = [IsOwnerPermission]
        elif self.action == 'partial_update':
            permission_classes = [IsOwnerPermission]
        elif self.action == 'destroy':
            permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
        elif self.action == 'create':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]
