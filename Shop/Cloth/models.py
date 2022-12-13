from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=150, blank=False)
    price = models.IntegerField(default=1)
    description = models.CharField(max_length=400, blank='This item has no description')

    def __str__(self):
        return f'Id {self.pk} {self.name} {self.price}'
