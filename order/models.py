from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel
from .choices import OrderStatus

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.SET_NULL, null=True, blank=True, related_name="orders")
    promocode = models.ForeignKey("promotions.Promocode", on_delete=models.SET_NULL, null=True, blank=True, related_name="orders")
    total_amount = models.BigIntegerField(null=False, blank=False)

    status = models.CharField(choices=OrderStatus.choices, default=OrderStatus.PENDING, null=False, blank=False)

    notes = models.CharField(max_length=255, null=True, blank=True)

    ordered_at = models.DateTimeField(auto_now_add=True)
    purchased_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Order<id={self.id}, price={self.total_price}>"

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")


class OrderItem(BaseModel):
    order = models.ForeignKey("order.Order", on_delete=models.RESTRICT, null=True, blank=True, related_name="items")
    product = models.ForeignKey("products.ProductVariant", on_delete=models.RESTRICT, null=True, blank=True, related_name="order_items")

    quantity = models.IntegerField(null=False, blank=False)
    price = models.BigIntegerField(null=False, blank=False)

    def __str__(self):
        return f"OrderItem <product_id={self.product_id}>"

    class Meta:
        verbose_name = _("Order Item")
        verbose_name_plural = _("Order Items")