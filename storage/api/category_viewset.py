from rest_framework import serializers, viewsets
from storage.models import Category
from ventasback.models import MyPageNumberPagination

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = MyPageNumberPagination
