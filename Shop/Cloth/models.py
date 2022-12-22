from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=150, blank=False)
    price = models.IntegerField(default=1)
    description = models.TextField(blank='This item has no description')
    item_img = models.OneToOneField('ProductImage', on_delete=models.PROTECT, default=None, null=True)

    def __str__(self):
        return f'Id {self.pk} {self.name} {self.price}'


class ProductImage(models.Model):
    image = models.ImageField(upload_to='item_photos')
