from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f'Status {self.name}'


class Order(models.Model):
    status = models.ForeignKey(Status, on_delete=models.PROTECT, blank=True, default=None)
    customer_name = models.CharField(max_length=100, blank=True, null=True, default=None)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=10, blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=True, auto_now=False)
    comments = models.TextField(blank=True, null=True, default=None)

    def __str__(self):
        return f'Order number {self.pk} have status {self.status}'

#
# class ItemInOrder(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.PROTECT, null=True, default=None)
#     product = models.ForeignKey(Item, on_delete=models.PROTECT, blank=True, null=True, default=None)
#
#     def __str__(self):
#         return f'{self.product.name}'
