from django.db import models
from django.core.validators import MinValueValidator

from ventasback.models import BaseModel
from storage.models import Product

class Order(BaseModel):
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    total_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(1)])
    
    # Foreign Keys
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='order_product')
    
    class Meta:
        ordering = ['id']