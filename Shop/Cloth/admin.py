from django.contrib import admin

from django.contrib import admin
from Cloth.models import Item


class ItemAdmin(admin.ModelAdmin):
    pass


admin.site.register(Item, ItemAdmin)
