from django.contrib import admin

from .models import Category, Provider, Product, Inventory
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    
    search_fields = ['name']
    list_filter = ['name']
    
admin.site.register(Category, CategoryAdmin)


class ProviderAdmin(admin.ModelAdmin):
    list_display = ['name', 'nit', 'phone']
    
    search_fields = ['name', 'nit', 'phone']
    list_filter = ['name', 'nit', 'phone']
    
admin.site.register(Provider, ProviderAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'product_type', 'category']
    
    search_fields = ['name', 'description', 'product_type']
    list_filter = ['name', 'description', 'product_type', 'category']
    
admin.site.register(Product, ProductAdmin)


class InventoryAdmin(admin.ModelAdmin):
    list_display = ['price', 'base_price', 'quantity', 'stock', 'provider', 'product']
    
    search_fields = ['price', 'base_price', 'quantity', 'stock']
    list_filter = ['price', 'base_price', 'quantity', 'stock', 'provider', 'product']
    
admin.site.register(Inventory, InventoryAdmin)
