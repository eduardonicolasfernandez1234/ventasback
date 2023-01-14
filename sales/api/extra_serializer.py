from rest_framework import serializers
from django.db.models import Model
from sales.models import Sales, Order, ReportSales
    
class OrderSimpleSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Order
        fields = '__all__'

class SalesSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = '__all__'

class ReportSalesSerializer(serializers.ModelSerializer):
    init_date = serializers.DateField(required=True)
    last_date = serializers.DateField(required=True)
    
    class Meta:
        model = ReportSales
        fields = '__all__'