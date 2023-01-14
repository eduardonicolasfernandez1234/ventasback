from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import serializers, viewsets, status
from rest_framework.exceptions import ValidationError
from django.db import transaction
from django.db.models import Sum, TextField
from django.db.models.functions import Coalesce
from django.http import JsonResponse

from sales.models import Sales, Order, ConfigSales
from sales.api import OrderSerializer, ConfigSalesSerializer, SalesSimpleSerializer, ReportSalesSerializer
from base.models import MyPageNumberPagination
from sales.repositories import SalesRepository
from authentication.models import User

class SalesSerializer(serializers.ModelSerializer):
    subtotal_amount = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)
    total_amount = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)
    
    config = ConfigSalesSerializer(read_only=True, many=False)
    config_id = serializers.PrimaryKeyRelatedField(
        many=False, write_only=True, queryset=ConfigSales.objects.filter(active=True), source='config', required=False
    )
    orders = OrderSerializer(read_only=True, many=True)
    orders_list = serializers.PrimaryKeyRelatedField(
        many=True, write_only=True, queryset=Order.objects.filter(order_state=Order.ORDER_PENDING), source='orders'
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
        
    @action(detail=True, methods=['get'], url_path="client",
            name="get all sales by client id")
    def sales_list_by_client(self, request, pk=None):
        if pk is None:
            return Response({
                "detail": "Missing foreign key",
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            User.objects.get(pk=pk, user_type=User.TYPE_CLIENT)
        except User.DoesNotExist:
            return Response({
                "detail": "Client not found",
            }, status=status.HTTP_404_NOT_FOUND)

        queryset = Sales.objects.filter(orders__client_id=pk)
        page = self.paginate_queryset(queryset)
        if page is not None:
                serializer = SalesSimpleSerializer(page, many=True, read_only=True)
                return self.get_paginated_response(serializer.data)
        else:
            serializer = SalesSimpleSerializer(queryset, many=True)
            return Response(serializer.data)
        
    @action(detail=False, methods=['post'], url_path="report-range-date",
            name="report sales by range date")
    def report_sales_by_range_date(self, request, pk=None):
        serializer = ReportSalesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        amount = Sales.objects.filter(
            created_at__range=[serializer['init_date'].value, serializer['last_date'].value]
        ).aggregate(
            amount=Coalesce(Sum('total_amount'), 0, output_field=TextField())
        )
        return JsonResponse(amount)