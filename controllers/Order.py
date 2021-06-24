
from models.Order import Order
from controllers.User import UserController
from controllers.Product import ProductController
from datetime import datetime


class OrderController():
    # Método construtor da classe UserController.
    def __init__(self):
        # Inicializa uma instância de User().
        self.order_model = Order()
        self.product_controller = ProductController()
        self.user_controller = UserController()

    def save_order(self, obj):
        self.order_model.product_fk = obj['product_id']
        self.order_model.user_fk = obj['user_id']
        self.order_model.quantity = obj['quantity']
        self.order_model.date_created = datetime.now()

        return self.order_model.save()