from django.shortcuts import render
from api.models import Customer
from rest_framework import viewsets
from .serializers import CustomerSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
