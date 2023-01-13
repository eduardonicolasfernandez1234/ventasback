from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    TYPE_CLIENT = 0
    TYPE_SUPERVISOR = 1
    TYPE_ADMIN = 2
    USER_TYPES = (
        (TYPE_CLIENT, 'client'),
        (TYPE_SUPERVISOR, 'supervisor'),
        (TYPE_ADMIN, 'admin'),
    )
    
    user_type = models.PositiveIntegerField(choices=USER_TYPES, default=TYPE_CLIENT)
    full_name = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    nit = models.CharField(max_length=13)
    birth_date = models.DateField(null=True, default=None)
