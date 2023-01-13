from django.db import models

from ventasback.models import BaseModel
from storage.models import Category

class Product(BaseModel):
    
    TYPE_PIECE = 0
    TYPE_BOX = 1
    TYPE_BAG = 2
    TYPE_ENVELOPES = 3
    TYPE_PACKAGES = 4
    OPTIONS_PRODUCT_TYPE = (
        (TYPE_PIECE, 'piece'),
        (TYPE_BOX, 'box'),
        (TYPE_BAG, 'bag'),
        (TYPE_ENVELOPES, 'envelopes'),
        (TYPE_PACKAGES, 'packages'),
    )
    
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=300, null=True)
    product_type = models.PositiveIntegerField(choices=OPTIONS_PRODUCT_TYPE, default=TYPE_PIECE)

    # Foreign Keys
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_category')
    
    class Meta:
        ordering = ['id']