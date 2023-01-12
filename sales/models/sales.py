from django.db import models
from django.core.validators import MinValueValidator

from ventasback.models import BaseModel
from sales.models import Order, ConfigSales

class Sales(BaseModel):
    subtotal_amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(1)])
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(1)])
    
    # Foreign Keys
    orders = models.ManyToManyField(Order, related_name='sales_orders')
    config = models.ForeignKey(ConfigSales, on_delete=models.CASCADE, related_name='sales_config')
    # client = models.ForeignKey('clients.Client', on_delete=models.CASCADE, related_name='sales_client')
    
    class Meta:
        ordering = ['id']