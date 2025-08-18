from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel
from .manager import UserManager

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    email = models.EmailField(max_length=255, unique=True, verbose_name=_("Email"))
    phone_number = models.CharField(unique=True, max_length=50, null=True, blank=True, verbose_name=_("Phone Number"))
    password = models.CharField(max_length=128, verbose_name=_("Password"))
    first_name = models.CharField(max_length=50, null=True, blank=True, verbose_name=_("First Name"))
    last_name = models.CharField(max_length=50, null=True, blank=True, verbose_name=_("Last Name"))
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True, verbose_name=_("Avatar"))

    profession = models.ForeignKey("users.Profession", on_delete=models.SET_NULL, null=True, blank=True, related_name="users", verbose_name=_("User Profession"))

    is_active = models.BooleanField(default=False, verbose_name=_("Is Active"))
    is_confirmed = models.BooleanField(default=False, verbose_name=_("Is Confirmed"))
    is_staff = models.BooleanField(default=False, verbose_name=_("Is Staff"))
    is_superuser = models.BooleanField(default=False, verbose_name=_("Is Superuser"))

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("User")
        ordering = ["-created_at"]

    def __str__(self):
        return self.email


class Profession(BaseModel):
    name = models.CharField(max_length=150, unique=True, verbose_name=_("Profession"))

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name