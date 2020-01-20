from django.contrib import admin

# Register your models here.



from django.contrib import admin

from priority.models import Clients
from .models import Order, OrderLineItem


class OrderLineAdminInline(admin.TabularInline):
    model = OrderLineItem


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInline, )

class ClientAdmin(admin.ModelAdmin):
    pass


admin.site.register(Order, OrderAdmin)
admin.site.register(Clients)

