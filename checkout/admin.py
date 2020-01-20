from django.contrib import admin
from priority.models import Clients
from .models import Order, OrderLineItem
from requestform.models import Jobs


class OrderLineAdminInline(admin.TabularInline):
    model = OrderLineItem

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInline, )

class ClientAdmin(admin.ModelAdmin):
    pass

class JobsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Order, OrderAdmin)
admin.site.register(Clients)
admin.site.register(Jobs)

