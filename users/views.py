from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny

from users.models import User
from .serializers import UserRegisterSerializer

# Create your views here.
class UserRegistrationAPIView(generics.CreateAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]
