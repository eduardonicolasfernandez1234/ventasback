from rest_framework import serializers, viewsets

from sales.models import Sales, Order, ConfigSales
from sales.api import OrderSerializer, ConfigSalesSerializer
from ventasback.models import MyPageNumberPagination

class SalesSerializer(serializers.Serializer):
    
    config = ConfigSalesSerializer(read_only=True, many=False)
    config_id = serializers.PrimaryKeyRelatedField(
        write_only=True, many=False, queryset=ConfigSales.objects.all(), source='config'
    )
    orders = OrderSerializer(read_only=True, many=True)
    orders_list = serializers.PrimaryKeyRelatedField(
        many=True, write_only=True, queryset=Order.objects.all(), source='orders'
    )
    
    class Meta:
        model = Sales
        field = '__all__'
        
class SalesViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
    pagination_class = MyPageNumberPagination