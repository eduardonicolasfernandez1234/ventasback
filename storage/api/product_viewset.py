from rest_framework import serializers, viewsets
from django.core.validators import MinValueValidator, MaxValueValidator

from ventasback.models import MyPageNumberPagination
from storage.models import Product, Category
from storage.api import CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    product_type = serializers.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)], required=True)
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