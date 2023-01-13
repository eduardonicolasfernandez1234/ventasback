from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import serializers, viewsets, status
from rest_framework.exceptions import ValidationError
from django.db import transaction

from sales.models import Sales, Order, ConfigSales
from sales.api import OrderSerializer, ConfigSalesSerializer
from ventasback.models import MyPageNumberPagination
from sales.repositories import SalesRepository

class SalesSerializer(serializers.ModelSerializer):
    subtotal_amount = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)
    total_amount = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)
    
    config = ConfigSalesSerializer(read_only=True, many=False)
    config_id = serializers.PrimaryKeyRelatedField(
        many=False, write_only=True, queryset=ConfigSales.objects.filter(active=True), source='config', required=False
    )
    orders = OrderSerializer(read_only=True, many=True)
    orders_list = serializers.PrimaryKeyRelatedField(
        many=True, write_only=True, queryset=Order.objects.all(), source='orders'
    )
    
    class Meta:
        model = Sales
        fields = '__all__'
        
class SalesViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
    pagination_class = MyPageNumberPagination
    
    @transaction.atomic()
    def create(self, request, *args, **kwargs):
        try:    
            with transaction.atomic():
                serializer = SalesSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                sales = serializer.save()
                SalesRepository.validate_orders_have_status_pending(sales.orders)
                SalesRepository.validate_orders_have_same_client(sales.orders)
                SalesRepository.validate_stock(sales.orders)
                SalesRepository.update_subtotal_sales(sales)
                SalesRepository.update_total_sales(sales)
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except ValidationError as v:
            return Response(v.detail, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)