from django.contrib import admin

from .models import Tax, Order, Sales, ConfigSales
# Register your models here.

class TaxAdmin(admin.ModelAdmin):
    list_display = ['name', 'percentage']
    
    search_fields = ['name', 'percentage']
    list_filter = ['name', 'percentage']
    
admin.site.register(Tax, TaxAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['quantity', 'total_price', 'inventory']
    
    search_fields = ['quantity', 'total_price']
    list_filter = ['quantity', 'total_price', 'inventory']
    
admin.site.register(Order, OrderAdmin)

class SalesAdmin(admin.ModelAdmin):
    list_display = ['subtotal_amount', 'total_amount', 'config']
    
    search_fields = ['subtotal_amount', 'total_amount']
    list_filter = ['subtotal_amount', 'total_amount']
    
admin.site.register(Sales, SalesAdmin)

class ConfigSalesAdmin(admin.ModelAdmin):
    list_display = ['name', 'active']
    
    search_fields = ['name', 'active']
    list_filter = ['name', 'active']
    
admin.site.register(ConfigSales, ConfigSalesAdmin)