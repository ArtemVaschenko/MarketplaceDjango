from django.contrib import admin

from order.models import Order, Status


class OrderAdmin(admin.ModelAdmin):
    pass


admin.site.register(Order, OrderAdmin)
admin.site.register(Status, OrderAdmin)
