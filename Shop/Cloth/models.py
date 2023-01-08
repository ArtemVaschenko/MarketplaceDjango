from django.db import models
from django.urls import reverse


class Item(models.Model):
    name = models.CharField(max_length=150, blank=False)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    price = models.IntegerField(default=1)
    description = models.TextField(blank='This item has no description')
    item_img = models.ForeignKey('ProductImage', on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return f'Id {self.pk} {self.name} {self.price}'

    def get_absolute_url(self):
        return reverse('item', kwargs={'item_slug': self.slug})


class ProductImage(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='static/item_photos')
    name = models.ForeignKey(Item, on_delete=models.PROTECT, blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return f' {self.image}'


class Category(models.Model):
    name = models.CharField(max_length=255, default=None, null=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    # items = models.ManyToOneRel('Item')

    def __str__(self):
        return f' {self.name}'
