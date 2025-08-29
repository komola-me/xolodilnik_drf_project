from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel
from .choices import TransactionStatus

# Create your models here.
class Transaction(BaseModel):
    order = models.ForeignKey(
        "order.Order", on_delete=models.CASCADE, verbose_name=_("order")
    )
    provider = models.ForeignKey(
        "payments.Provider",
        on_delete=models.CASCADE,
        verbose_name=_("Provider"),
        related_name="transactions",
    )
    status = models.CharField(
        max_length=10,
        choices=TransactionStatus.choices,
        default=TransactionStatus.PENDING,
        verbose_name=_("Status"),
    )
    paid_at = models.DateTimeField(null=True, blank=True, verbose_name=_("Paid at"))
    cancelled_at = models.DateTimeField(
        null=True, blank=True, verbose_name=_("Cancelled at")
    )
    amount = models.DecimalField(
        max_digits=12, decimal_places=2, verbose_name=_("Amount")
    )

    def __str__(self):
        return f"Transaction: {self.id}"

    class Meta:
        verbose_name = _("Transaction")
        verbose_name_plural = _("Transactions")


class Provider(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Provider Name"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Provider")
        verbose_name_plural = _("Providers")
