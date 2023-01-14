from rest_framework import serializers, viewsets, status
from rest_framework.response import Response

from authentication.api import UserSerializer
from authentication.models import User
from sales.models import Order
from storage.api import InventorySerializer
from storage.models import Inventory
from base.models import MyPageNumberPagination


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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        order.order_state = Order.ORDER_PENDING
        order.save()
        headers = self.get_success_headers(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)