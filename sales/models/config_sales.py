from django.db import models

from ventasback.models import BaseModel
from sales.models import Tax

class ConfigSales(BaseModel):
    name = models.CharField(max_length=50)
    # Foreign Keys
    taxes = models.ManyToManyField(Tax, related_name='config_sales_taxes')
    
    class Meta:
        ordering = ['id']
        