from rest_framework import serializers, viewsets

from ventasback.models import MyPageNumberPagination
from sales.models import Tax

class TaxSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tax
        fields = '__all__'

class TaxViewSet(viewsets.ModelViewSet):
    queryset = Tax.objects.all()
    serializer_class = TaxSerializer
    pagination_class = MyPageNumberPagination