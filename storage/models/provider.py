from django.db import models

from ventasback.models import BaseModel

class Provider(BaseModel):
    name = models.CharField(max_length=150)
    nit = models.CharField(max_length=13, unique=True)
    phone = models.CharField(max_length=20, null=True, default=None)
    
    class Meta:
        ordering = ['id']
