from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
import jwt
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status

from users.models import User
from .serializers import UserRegisterSerializer

# Create your views here.
class UserRegistrationAPIView(generics.CreateAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]


class EmailConfirmationAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        token = kwargs.get("token")
        decoded = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
        try:
            user = User.objects.get(id=decoded.get("user_id"))
        except User.DoesNotExist:
            return Response(data={"status": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        user.is_confirmed = True
        user.save()

        return Response(data={"status": "User has been confirmed"}, status=status.HTTP_200_OK)