from django.db import models

from Cloth.models import Item


class Order(models.Model):
    customer_name = models.CharField(max_length=100, blank=True, null=True, default=None)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=10, blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=True, auto_now=False)
    comments = models.TextField(blank=True, null=True, default=None)

    def __str__(self):
        return f'Order number {self.pk}'


class ItemInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, null=True, default=None)
    product = models.ForeignKey(Item, on_delete=models.PROTECT, blank=True, null=True, default=None)

    def __str__(self):
        return f'{self.product.name}'
