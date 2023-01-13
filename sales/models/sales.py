from django.db import models
from django.core.validators import MinValueValidator
from rest_framework.exceptions import ValidationError

from ventasback.models import BaseModel
from sales.models import Order, ConfigSales

class Sales(BaseModel):
    SALES_ACTIVE = 0
    SALES_CANCELED = 1
    SALES_STATES = (
        (SALES_ACTIVE, 'pending'),
        (SALES_CANCELED, 'canceled'),
    )
    
    sales_state = models.PositiveIntegerField(choices=SALES_STATES, default=SALES_ACTIVE)
    subtotal_amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], default=0)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], default=0)
    
    # Foreign Keys
    orders = models.ManyToManyField(Order, related_name='sales_orders')
    config = models.ForeignKey(ConfigSales, on_delete=models.CASCADE, related_name='sales_config')
    
    class Meta:
        ordering = ['id']
        
    def save(self, *args, **kwargs):
        try:
            self.config = ConfigSales.objects.get(active=True)
        except ConfigSales.DoesNotExist:
            raise ValidationError({
                'res': 'error',
                'detail': 'No existe una configuración activa para las ventas, activar una e intente nuevamente'
            })
        super(Sales, self).save(*args, **kwargs)