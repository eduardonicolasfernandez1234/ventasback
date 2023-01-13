from rest_framework.exceptions import ValidationError
import decimal

from sales.models import Order

class SalesRepository:
    @staticmethod
    def validate_stock(orders):
        """Validate current stock for all orders based on associated inventory.

        Args:
            orders: Needs a queryset that contains a list of orders.

        """
        [SalesRepository._validate_product(order) for order in orders.all()]
    
    @staticmethod
    def _validate_product(order):
        """Private function to validate an order based on the associated inventory.

        Args:
            order: Needs a queryset that contains an order.

        """
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
        """Validate if all orders have the same client.

        Args:
            order: Needs a queryset that contains a list of orders.

        """
        has_same_client = len(set([order.client.id for order in orders.all()])) == 1
        if not has_same_client:
            raise ValidationError({
                'detail': 'Los pedidos deben de tener el mismo cliente'
            })    
    
    @staticmethod
    def validate_orders_have_status_pending(orders):
        """Validate if all orders have pending status.

        Args:
            order: Needs a queryset that contains a list of orders.

        """
        has_same_client = all([order.order_state == Order.ORDER_PENDING for order in orders.all()])
        if not has_same_client:
            raise ValidationError({
                'detail': 'Todos los pedidos deben de tener el estado pendiente'
            })    

    @staticmethod
    def update_subtotal_sales(sales):
        """Calculate the subtotal of all orders in a sale.

        Args:
            sales: Needs a queryset that contains an sales object.

        """
        sales.subtotal_amount = sum([order.total_price for order in sales.orders.all()])
        sales.save()
    
    @staticmethod
    def update_total_sales(sales):
        """Calculate the total of the sale applying tax rates.

        Args:
            sales: Needs a queryset that contains an sales object.

        """
        taxes = sales.config.taxes.all()
        total_taxes = 0
        for tax in taxes:
            total_taxes += sales.subtotal_amount * (tax.percentage / decimal.Decimal(100))
        sales.total_amount = sales.subtotal_amount + total_taxes
        sales.save()