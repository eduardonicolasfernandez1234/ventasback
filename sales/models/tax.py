from django.db import models
from django.core.validators import MinValueValidator

from ventasback.models import BaseModel

class Tax(BaseModel):
    name = models.CharField(max_length=50)
    percentage = models.DecimalField(max_digits=4, decimal_places=2, validators=[MinValueValidator(1)])
    
    class Meta:
        ordering = ['id']