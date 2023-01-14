from django.db import models

from base.models import BaseModel
from base.validations import TitleField


class Category(BaseModel):
    name = TitleField(max_length=150, unique=True)

    class Meta:
        ordering = ['id']

    def __str__(self) -> str:
        return f"{self.id}.- {self.name}"
