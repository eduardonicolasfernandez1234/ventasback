from rest_framework import serializers, viewsets, status
from rest_framework.response import Response

from sales.models import Tax, ConfigSales
from sales.api import TaxSerializer
from base.models import MyPageNumberPagination

class ConfigSalesSerializer(serializers.ModelSerializer):
    taxes = TaxSerializer(read_only=True, many=True)
    taxes_list = serializers.PrimaryKeyRelatedField(
        many=True, write_only=True, queryset=Tax.objects.all(), source='taxes'
    )
    
    class Meta:
        model = ConfigSales
        fields = '__all__'
        
class ConfigSalesViewSet(viewsets.ModelViewSet):
    queryset = ConfigSales.objects.all()
    serializer_class = ConfigSalesSerializer
    pagination_class = MyPageNumberPagination
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        config_sales = serializer.save()
        if config_sales.active:
            ConfigSales.objects.exclude(id=config_sales.id).update(active=False)
        headers = self.get_success_headers(config_sales)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        config_sales = serializer.save()
        if config_sales.active:
            ConfigSales.objects.exclude(id=config_sales.id).update(active=False)
        headers = self.get_success_headers(config_sales)
        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)