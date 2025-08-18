from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel

# Create your models here.
class Product(BaseModel):
    name = models.CharField(max_length=200, verbose_name=_("Name"))
    image = models.ImageField(upload_to="products/", verbose_name=_("Image"))

    category = models.ForeignKey("products.Categort", on_delete=models.RESTRICT, related_name="products", verbose_name=_("Product Category"))

    is_featured = models.BooleanField()
    is_active = models.BooleanField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")


class ProductVariant(BaseModel):
    product = models.ForeignKey("products.Product", on_delete=models.RESTRICT, related_name="variants", verbose_name="Product Variant")
    name = models.CharField(max_length=150, verbose_name=_("Name"))
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="product_variants/")

    is_active = models.BooleanField()
    is_featured = models.BooleanField()

    rating = models.CharField()
    sold_count = models.PositiveIntegerField()

    class Meta:
        unique_together = ("product", "name")
        ordering = ["product__name", "name"]

    def __str__(self):
        return f"{self.product.name} - {self.name}"


class Category(BaseModel):
    name = models.CharField(max_length=150, unique=True, verbose_name=_("Category"))

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name