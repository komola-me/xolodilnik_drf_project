from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel
from .manager import UserManager

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    email = models.EmailField(max_length=255, unique=True, verbose_name=_("Email"))
    phone_number = models.CharField(unique=True, max_length=50, null=True, blank=True, verbose_name=_("Phone Number"))
    first_name = models.CharField(max_length=50, null=True, blank=True, verbose_name=_("First Name"))
    last_name = models.CharField(max_length=50, null=True, blank=True, verbose_name=_("Last Name"))
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True, verbose_name=_("Avatar"))

    profession = models.ForeignKey("users.Profession", on_delete=models.RESTRICT, null=True, blank=True, related_name="users", verbose_name=_("User Profession"))
    wishlist = models.ManyToManyField(
        "products.ProductVariant",
        through="Wishlist",
        through_fields=("user", "product_variant"),
        related_name="user_wishlist",
        verbose_name=_("wishlist"),
    )

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


class Wishlist(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name='wishlist_items')
    product_variant = models.ForeignKey("products.ProductVariant", on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product_variant')

    def __str__(self):
        return f"{self.user} - {self.product_variant}"


class UserFeedback(BaseModel):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="feedbacks", verbose_name=_("user"))

    message = models.CharField(max_length=500, verbose_name=_("message"))

    def __str__(self):
        return f"{self.user} - {self.message}"

    class Meta:
        verbose_name = _("User Feedback")
        verbose_name_plural = _("User Feedback")