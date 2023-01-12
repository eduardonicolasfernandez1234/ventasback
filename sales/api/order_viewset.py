from rest_framework import serializers, viewsets
from sales.models import Order
from ventasback.models import MyPageNumberPagination

from storage.models import Product
from storage.api import ProductSerializer

class OrderSerializer(serializers.Serializer):
    product = ProductSerializer(read_only=True, many=False)
    product_id = serializers.PrimaryKeyRelatedField(
        write_only=True, many=False, queryset=Product.objects.all(), source='product'
    )
    
    class Meta:
        model = Order
        field = '__all__'
        
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = MyPageNumberPagination