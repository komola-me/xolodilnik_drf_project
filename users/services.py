from .models import Profession

def update_user_with_profession(user, validated_data):
    profession_data = validated_data.pop("profession", None)

    if profession_data:
        profession, _ = Profession.objects.get_or_create(name=profession_data["name"])
        user.profession = profession
    elif profession_data is None:
        user.profession = None

    for attr, value in validated_data.items():
        setattr(user, attr, value)

    user.save()
    return user