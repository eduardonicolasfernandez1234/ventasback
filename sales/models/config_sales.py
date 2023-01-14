from django.db import models

from base.models import BaseModel
from sales.models import Tax

class ConfigSales(BaseModel):
    name = models.CharField(max_length=50)
    active = models.BooleanField(default=False)
    # Foreign Keys
    taxes = models.ManyToManyField(Tax, related_name='config_sales_taxes')
    
    class Meta:
        ordering = ['id']
        
    def __str__(self) -> str:
        return f"{self.id}.- {self.name} - {str(self.taxes)}"