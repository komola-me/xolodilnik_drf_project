from django.db import models
from django.utils.translation import gettext_lazy as _


class TransactionStatus(models.TextChoices):
    PENDING = "pending", _("Pending")
    PAID = "paid", _("Paid")
    CANCELLED = "cancelled", _("Cancelled")
    FAILED = "failed", _("Failed")