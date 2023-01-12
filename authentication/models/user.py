from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    CLIENT = 0
    SUPERVISOR = 1
    ADMIN = 2
    USER_TYPES = (
        (CLIENT, 'client'),
        (SUPERVISOR, 'supervisor'),
        (ADMIN, 'admin'),
    )
    
    user_type = models.PositiveIntegerField(choices=USER_TYPES, default=CLIENT)
    full_name = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    nit = models.CharField(max_length=13)
    birth_date = models.DateField(null=True, default=None)
