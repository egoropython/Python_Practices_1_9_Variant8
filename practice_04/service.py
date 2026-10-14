from models import Order
from exceptions import OrderNotFoundError

class OrderService:
    def __init__(self, storage):
        self.storage = storage
        self.orders = storage.load()

    def create(self, customer, items):
        if not customer.strip(): raise ValueError("Имя клиента не должно быть пустым.")
        if not items: raise ValueError("Заказ должен содержать хотя бы один товар.")
        for item in items:
            if float(item["price"]) < 0 or int(item["quantity"]) <= 0:
                raise ValueError("Цена должна быть неотрицательной, количество — положительным.")
        number = max((int(order["number"]) for order in self.orders), default=0) + 1
        order = Order(number, customer.strip(), items)
        self.orders.append(order.to_dict()); self.storage.save(self.orders)
        return order.to_dict()

    def _find(self, number):
        for order in self.orders:
            if int(order["number"]) == int(number): return order
        raise OrderNotFoundError(f"Заказ №{number} не найден.")

    def change_status(self, number, status):
        allowed = {"новый", "оплачен", "отправлен", "отменён"}
        if status not in allowed: raise ValueError("Недопустимый статус заказа.")
        order = self._find(number); order["status"] = status; self.storage.save(self.orders); return order

    def cancel(self, number): return self.change_status(number, "отменён")
    def search(self, number): return self._find(number)
    def all_orders(self): return list(self.orders)
