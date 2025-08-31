from django.urls import path

from users.views import (
    UserRegistrationAPIView,
    EmailConfirmationAPIView
    )

urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='register'),
    path('register/confirm/<str:token>/', EmailConfirmationAPIView.as_view(), name="register-confirm"),
]