from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel

# Create your models here.
class Product(BaseModel):
    name = models.CharField(max_length=200, verbose_name=_("Name"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("price"))
    image = models.ImageField(upload_to="products/", verbose_name=_("Image"))

    category = models.ForeignKey("products.Category", on_delete=models.RESTRICT, related_name="products", verbose_name=_("Product Category"))

    is_featured = models.BooleanField(default=False, verbose_name=_("Is Featured"))
    is_active = models.BooleanField(default=False, verbose_name=_("Is Active"))

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
    color = models.CharField(max_length=100, null=True, blank=True, verbose_name=_("color"))
    size = models.CharField(max_length=100, null=True, blank=True, verbose_name=_("size"))
    image = models.ImageField(upload_to="product_variants/")

    is_active = models.BooleanField(default=True, verbose_name=_("is active"))
    is_featured = models.BooleanField(default=False, verbose_name=_("is featured"))

    rating = models.CharField(null=True, blank=True, verbose_name=_("rating"))
    sold_count = models.PositiveIntegerField(blank=True, null=True, default=0, verbose_name=_("Sold Count"))

    class Meta:
        verbose_name = _("Product Variant")
        verbose_name_plural = _("Product Variants")
        unique_together = ("product", "name")
        ordering = ["product__name", "name"]

    def __str__(self):
        return f"{self.product.name} - {self.color} - {self.size}"


class Category(BaseModel):
    name = models.CharField(max_length=40, unique=True, verbose_name=_("Category"))
    description = models.CharField(max_length=500, blank=True, verbose_name=_("Description"))

    image = models.ImageField(upload_to="categories/", blank=True, null=True, verbose_name=_("image"))

    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"))

    class Meta:
        ordering = ["name"]
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name