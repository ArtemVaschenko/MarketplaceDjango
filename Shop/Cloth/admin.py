from django.contrib import admin

from django.contrib import admin
from Cloth.models import Item, ProductImage


class ItemAdmin(admin.ModelAdmin):
    pass


admin.site.register(Item, ItemAdmin)
admin.site.register(ProductImage, ItemAdmin)