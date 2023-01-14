from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from base.models import BaseModel

class Tax(BaseModel):
    name = models.CharField(max_length=50)
    percentage = models.DecimalField(max_digits=4, decimal_places=2, validators=[MinValueValidator(1), MaxValueValidator(99)])
    
    class Meta:
        ordering = ['id']
        
    def __str__(self):
        return f"{self.id}.- {self.name} - {self.percentage}%"