from django.db import models

from ventasback.models import BaseModel

class Category(BaseModel):
    name = models.CharField(max_length=150, unique=True)
    
    class Meta:
        ordering = ['id']