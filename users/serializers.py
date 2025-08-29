from rest_framework import serializers

from .models import User

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

        return user
