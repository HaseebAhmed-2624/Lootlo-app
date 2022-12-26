from rest_framework import viewsets
from django.contrib.auth import get_user_model
from api.serializers import UserSerializer
from rest_framework import permissions
from api.permissions import IsOwnerPermission


class UserModelViewSet(viewsets.ModelViewSet):
    User = get_user_model()
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [permissions.IsAdminUser]
        elif self.action == 'retieve':
            permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
        elif self.action == 'update':
            permission_classes = [IsOwnerPermission]
        elif self.action == 'partial_update':
            permission_classes = [IsOwnerPermission]
        elif self.action == 'destroy':
            permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
        elif self.action == 'create':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

 # TODO create user type model
 # TODO write tests for code
 # TODO handle errors

