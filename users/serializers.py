from rest_framework import serializers

from .models import User, Profession
from .tasks import send_register_email
from .services import update_user_with_profession


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ["id", "name"]


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


class UserProfileSerializer(serializers.ModelSerializer):
    profession = ProfessionSerializer()

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "username",
            "first_name",
            "last_name",
            "phone_number",
            "avatar",
            "profession",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ("id", "username", "email")

    def update(self, instance, validated_data):
        return update_user_with_profession(instance, validated_data)