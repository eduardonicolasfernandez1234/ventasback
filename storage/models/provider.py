from django.db import models

from base.models import BaseModel
from base.validations import TitleField

class Provider(BaseModel):
    name = TitleField(max_length=150)
    nit = models.CharField(max_length=13, unique=True)
    phone = models.CharField(max_length=20, null=True, default=None)
    
    class Meta:
        ordering = ['id']
