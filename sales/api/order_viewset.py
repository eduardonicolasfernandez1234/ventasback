from rest_framework import serializers, viewsets
from rest_framework.exceptions import ValidationError
from django.db import transaction

from ventasback.models import MyPageNumberPagination
from sales.models import Order
from storage.models import Inventory
from storage.api import InventorySerializer
from authentication.models import User
from authentication.api import UserSerializer

class OrderSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(required=True)
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)

    inventory = InventorySerializer(read_only=True, many=False)
    inventory_id = serializers.PrimaryKeyRelatedField(
        write_only=True, many=False, queryset=Inventory.objects.all(), source='inventory'
    )
    client = UserSerializer(read_only=True, many=False)
    client_id = serializers.PrimaryKeyRelatedField(
        write_only=True, many=False, queryset=User.objects.filter(user_type=User.TYPE_CLIENT), source='client'
    )
    
    class Meta:
        model = Order
        fields = '__all__'
        
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = MyPageNumberPagination

    # @transaction.atomic()
    # def create(self, request, *args, **kwargs):
    #     serializer = OrderSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     order = serializer.save()
        
    #     inventory = Inventory.objects.filter(product_id=order.product.id)
        
    #     quantity_inventory = sum([inv.stock for inv in inventory])
        
    #     if quantity_inventory < order.quantity:
    #         raise ValidationError({
    #             'res': 'error',
    #             'detail': f'No hay suficiente stock para el producto {order.product.name}'
    #         })
        
    #     for inv in inventory:
    #         if order.quantity <= inv.stock:
    #             inv.stack = inv.stock - order.quantity

    #     # raise ValidationError({
    #     #             'res': 'error',
    #     #             'detail': f'No hay suficiente stock para el producto {order.product.name}'
    #     #         })
    #     taxes = self.config.taxes
    #     for tax in taxes:
    #         self.total_amount += self.subtotal_amount * tax.percentage
    #     super(Sales, self).save(*args, **kwargs)
        
        
    # def updateStockInventory(self, inventory, quantity):
    #     if quantity <= 0:
    #         return
    #     check_quantity = inventory.stock - quantity
    #     if check_quantity < 0:
    #         inventory.stock = 0
    #     else:
    #         inventory.stock = inventory.stock - quantity
    #     inventory.save()
    #     return abs(check_quantity)