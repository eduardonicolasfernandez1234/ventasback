from django.db import models

from ventasback.models import BaseModel
from ventasback.validations import TitleField

class Category(BaseModel):
    name = TitleField(max_length=150, unique=True)
    
    class Meta:
        ordering = ['id']