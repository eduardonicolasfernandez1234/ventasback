from django.contrib import admin

from .models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'address', 'email', 'phone', 'nit', 'birth_date', 'user_type', 'is_staff', 'is_active']
    
    search_fields = ['full_name', 'address', 'email', 'phone', 'nit', 'birth_date', 'user_type', 'is_staff', 'is_active']
    list_filter = ['full_name', 'address', 'email', 'phone', 'nit', 'birth_date', 'user_type', 'is_staff', 'is_active']
    
admin.site.register(User, UserAdmin)
