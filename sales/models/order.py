from django.db import models
from django.core.validators import MinValueValidator
from rest_framework.exceptions import ValidationError

from ventasback.models import BaseModel
from storage.models import Inventory
from authentication.models import User

class Order(BaseModel):
    ORDER_PENDING = 0
    ORDER_APPROVED = 1
    ORDER_CANCELED = 2
    ORDER_STATES = (
        (ORDER_PENDING, 'pending'),
        (ORDER_APPROVED, 'approved'),
        (ORDER_CANCELED, 'canceled'),
    )
    
    order_state = models.PositiveIntegerField(choices=ORDER_STATES, default=ORDER_PENDING)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    total_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(1)])
    
    # Foreign Keys
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, related_name='order_inventory')
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_client')
    
    class Meta:
        ordering = ['id']

    def save(self, *args, **kwargs):
        try:
            inventory = Inventory.objects.get(id=self.inventory_id)
        except Inventory.DoesNotExist:
            raise ValidationError({
                'res': 'error',
                'detail': f'El producto no existe en el inventario'
            })

        if inventory.stock < self.quantity:
            raise ValidationError({
                'res': 'error',
                'detail': f'No hay suficiente stock para el producto {self.inventory.product.name}'
            })
        self.total_price = inventory.price * self.quantity
        super(Order, self).save(*args, **kwargs)
