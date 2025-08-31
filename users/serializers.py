from rest_framework import serializers

from .models import User
from .tasks import send_register_email

class UserRegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
    password_confirm = serializers.CharField(required=True)

    def validate(self, data):
        if data["password"] != data["password_confirm"]:
            raise serializers.ValidationError("Passwords do not match!")
        return data

    def save(self, **kwargs):
        user = User.objects._create_user(
            email=self.validated_data["email"],
            password=self.validated_data["password"],
            is_confirmed=False,
        )

        send_register_email.delay(user_id=user.id, email=user.email)

        return user
