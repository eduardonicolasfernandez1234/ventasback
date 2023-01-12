from django.db import models

from ventasback.models import BaseModel
from storage.models import Category

class Product(BaseModel):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=300, null=True)
    product_type = models.PositiveIntegerField(default=0)

    # Foreign Keys
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_category')
    
    class Meta:
        ordering = ['id']