from rest_framework import serializers, viewsets

from sales.models import Tax, ConfigSales
from sales.api import TaxSerializer
from ventasback.models import MyPageNumberPagination

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