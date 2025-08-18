from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from common.models import BaseModel

# Create your models here.
class PromotionType(models.TextChoices):
    PERCENTAGE = "percentage", _("Percentage")
    FIXED = "fixed", _("Fixed Amount")


class Promocode(BaseModel):
    code = models.CharField(max_length=50, unique=True, verbose_name=_("Code"))
    description = models.TextField(blank=True, verbose_name=_("Description"))

    type = models.CharField(max_length=20, choices=PromotionType.choices, default=PromotionType.PERCENTAGE, verbose_name=_("Type"))
    value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Value"))

    min_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name=_("Minimum Order Amount"))
    usage_limit = models.PositiveIntegerField(null=True, blank=True, verbose_name=_("Max Usage (global)"))

    valid_from = models.DateTimeField(verbose_name=_("Valid From"))
    valid_until = models.DateTimeField(verbose_name=_("Valid Until"))
    is_active = models.BooleanField(default=True, verbose_name=_("Active"))

    def is_valid(self):
        now = timezone.now()
        return (
            self.is_active
            and self.valid_from <= now <= self.valid_until
            and (self.usage_limit is None or self.usages.count() < self.usage_limit)
        )

    class Meta:
        verbose_name = _("Promo Code")
        verbose_name_plural = _("Promo Codes")
        ordering = ["-created_at"]

    def __str__(self):
        return self.code


class PromocodeUsage(BaseModel):
    promocode = models.ForeignKey(Promocode, on_delete=models.CASCADE, related_name="usages", verbose_name=_("Promo Code"))
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="promocode_usages", verbose_name=_("User"))
    used_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Used At"))

    class Meta:
        verbose_name = _("Promo Code Usage")
        verbose_name_plural = _("Promo Code Usages")
        unique_together = ("promocode", "user")

    def __str__(self):
        return f"{self.user} used {self.promocode.code}"


class DiscountType(models.TextChoices):
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE, related_name="discounts", verbose_name=_("Product"))

    name = models.CharField(max_length=150, verbose_name=_("Discount Name"))
    description = models.TextField(blank=True, null=True, verbose_name=_("Description"))

    type = models.CharField(max_length=20, choices=PromotionType.choices, default=PromotionType.PERCENTAGE, verbose_name=_("Discount Type"))
    value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Discount Value"))

    valid_from = models.DateTimeField(verbose_name=_("Valid From"))
    valid_until = models.DateTimeField(verbose_name=_("Valid Until"))
    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"))

    class Meta:
        verbose_name = _("Discount")
        verbose_name_plural = _("Discounts")
        ordering = ["-valid_from"]

    def __str__(self):
        return f"{self.name} ({self.type}) for {self.product}"
