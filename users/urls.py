from django.urls import path

from users.views import (
    UserRegistrationAPIView,
    )

urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='register'),
]