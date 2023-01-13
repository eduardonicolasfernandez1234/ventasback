import decimal

from sales.models import Order
from storage.models import Inventory

from rest_framework.exceptions import ValidationError

class SalesRepository:
    @staticmethod
    def validate_stock(orders):
        [SalesRepository._validate_product(order) for order in orders.all()]
    
    @staticmethod
    def _validate_product(order):
        inventory = order.inventory
        if inventory.stock >= order.quantity:
            inventory.stock = inventory.stock - order.quantity
            inventory.save()
            
            order.order_state = Order.ORDER_APPROVED
            order.save()
        else:
            raise ValidationError({
                'res': 'error',
                'detail': f'El producto {order.product.name} no tiene stock suficiente'
            })
            
    @staticmethod
    def validate_orders_have_same_client(orders):
        has_same_client = len(set([order.client.id for order in orders.all()])) == 1
        if not has_same_client:
            raise ValidationError({
                'detail': 'Los pedidos deben de tener el mismo cliente'
            })    
    
    @staticmethod
    def validate_orders_have_status_pending(orders):
        has_same_client = all([order.order_state == Order.ORDER_PENDING for order in orders.all()])
        if not has_same_client:
            raise ValidationError({
                'detail': 'Todos los pedidos deben de tener el estado pendiente'
            })    

    @staticmethod
    def update_subtotal_sales(sales):
        sales.subtotal_amount = sum([order.total_price for order in sales.orders.all()])
        sales.save()