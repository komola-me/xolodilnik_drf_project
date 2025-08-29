from django.db import models
from django.utils.translation import gettext_lazy as _

class PromotionType(models.TextChoices):
    PERCENTAGE = "percentage", _("Percentage")
    FIXED = "fixed", _("Fixed Amount")