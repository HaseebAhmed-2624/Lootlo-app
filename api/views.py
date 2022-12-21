# from django.shortcuts import render
# from api.models import Customer, Seller, Admin
# from rest_framework import viewsets
# from .serializers import CustomerSerializer, SellerSerializer, AdminSerializer
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework.permissions import IsAuthenticated
#
#
# # Create your views here.
# class CustomerViewSet(viewsets.ModelViewSet):
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer
#     permission_classes = [IsAuthenticated]
#     authentication_classes = [JWTAuthentication]
#
#
# class SellerViewSet(viewsets.ModelViewSet):
#     queryset = Seller.objects.all()
#     serializer_class = SellerSerializer
#     permission_classes = [IsAuthenticated]
#     authentication_classes = [JWTAuthentication]
#
#
# class AdminViewSet(viewsets.ModelViewSet):
#     queryset = Admin.objects.all()
#     serializer_class = AdminSerializer
#     permission_classes = [IsAuthenticated]
#     authentication_classes = [JWTAuthentication]

from rest_framework import views
from rest_framework.response import Response

# class LoginUserAPI(views.APIView):
#     def post(self,request):
#         serializer=