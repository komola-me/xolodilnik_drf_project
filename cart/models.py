from django.db import models
from django.utils.translation import gettext_lazy as _

from products.models import Product

# Create your models here.
class UserCart(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name='cart', verbose_name=_("User"))

    def __str__(self):
        return f"Cart for {self.user}"

    class Meta:
        verbose_name = _("Cart")
        verbose_name_plural = _("Carts")


class CartItem(models.Model):
    cart = models.ForeignKey(UserCart, on_delete=models.CASCADE, related_name="cart_items", verbose_name=_("Cart"))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="cart_items", verbose_name=_("Product"))

    quantity = models.PositiveIntegerField(default=1, verbose_name=_("Quantity"))
    price_at_time = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    class Meta:
        verbose_name = _("Cart Item")
        verbose_name_plural = _("Cart Items")
