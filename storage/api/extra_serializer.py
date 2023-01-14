from rest_framework import serializers
from django.core.validators import MinValueValidator
from storage.models import Inventory, Product, Provider, Category


class InventoryFilterSerializer(serializers.ModelSerializer):
    price_init = serializers.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], default=None, allow_null=True)
    price_last = serializers.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], default=None, allow_null=True)
    stock_init = serializers.IntegerField(
        validators=[MinValueValidator(0)], default=None, allow_null=True)
    stock_last = serializers.IntegerField(
        validators=[MinValueValidator(0)], default=None, allow_null=True)
    provider = serializers.CharField(max_length=150, default=None, allow_null=True)
    product = serializers.CharField(max_length=150, default=None, allow_null=True)
    category = serializers.CharField(max_length=150, default=None, allow_null=True)
    
    price = serializers.IntegerField(required=False)
    base_price = serializers.IntegerField(required=False)
    quantity = serializers.IntegerField(required=False)

    class Meta:
        model = Inventory
        fields = '__all__'
