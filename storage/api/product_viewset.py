from rest_framework import serializers, viewsets
from ventasback.models import MyPageNumberPagination
from storage.models import Product, Category
from storage.api import CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True, many=False)
    category_id = serializers.PrimaryKeyRelatedField(
        write_only=True, many=False, queryset=Category.objects.all(), source='category'
    )
    
    class Meta:
        model = Product
        fields = '__all__'

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = MyPageNumberPagination