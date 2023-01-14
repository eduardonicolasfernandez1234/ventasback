from django.db import models

from base.models import BaseModel

class ReportSales(BaseModel):
    init_date = models.DateField()
    last_date = models.DateField()
