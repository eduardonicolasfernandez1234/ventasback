from django.db import models
from django.core.validators import MinValueValidator

from ventasback.models import BaseModel
from storage.models import Provider, Product

class Inventory(BaseModel):
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    base_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    quantity = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    stock = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    
    # Foreign key
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name='store_provider')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='store_product')
    
    class Meta:
        ordering = ['id']
        
    def save(self, *args, **kwargs):
            self.stock = self.quantity
            super(Inventory, self).save(*args, **kwargs)