from rest_framework import viewsets, status, permissions
from django.contrib.auth import get_user_model
from api.permissions import IsOwnerPermission
from django.core.signals import request_started
from django.dispatch import receiver
from api.models import UserType, CustomUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import UserSerializer



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
        return [auth() for auth in self.authentication_classes]

    def get_permissions(self):

        """Assigning permissions for actions in ModelViewSet"""

        if self.action == 'retrieve':
            permission_classes = [IsOwnerPermission]
        elif self.action == 'list':
            permission_classes = [permissions.IsAdminUser]
            print()
        elif self.action == 'update':
            permission_classes = [IsOwnerPermission]
        elif self.action == 'partial_update':
            permission_classes = [IsOwnerPermission]
        elif self.action == 'destroy':
            permission_classes = [IsOwnerPermission]
        elif self.action == 'create':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

    def update(self, request, *args, **kwargs):
        """get user id from token and perform update operation"""
        response = JWTAuthentication().authenticate(request)
        if response is not None:
            user, token = response
            id = token.get('user_id', default=None)
            if id is None:
                return Response(data="Invalid Token")
            else:
                instance = CustomUser.objects.get(pk=id)
                serializer = self.get_serializer(instance, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(data={'message': 'Record Update'})
                else:
                    return Response(data=serializer.errors)

    def retrieve(self, request, *args, **kwargs):
        """get user id from token and perform retrieve operation"""
        response = JWTAuthentication().authenticate(request)
        if response is not None:
            user, token = response
            id = token.get('user_id', default=None)
            if id is None:
                return Response(data={'message': "Invalid Token"})
            else:
                instance = CustomUser.objects.get(pk=id)
                serializer = UserSerializer(instance=instance)
            return Response(data=serializer.data)
        else:
            return Response(data={'message': "authentication credentials were not provided"})

    def destroy(self, request, *args, **kwargs):
        """get user id from token and perform delete operation"""

        response = JWTAuthentication().authenticate(request)
        if response is not None:
            token = response[1]
            id = token.get('user_id', default=None)
            if id is None:
                return Response(data={'message': "Invalid Token"})
            else:
                instance = CustomUser.objects.get(pk=id)
                instance.delete()
            return Response(data={'message': 'User Deleted'})
        else:
            return Response(data={'message': "authentication credentials were not provided"})


class VerifyToken(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    """

    def post(self, request, format=None):
        """
        Return a list of all users.
        """
        response = JWTAuthentication().authenticate(request)
        if response is not None:
            user, token = response
            return Response(data={'message': f'this is decoded token claims  {token.payload}'})
        else:
            return Response(data={'message': "authentication credentials were not provided"})
