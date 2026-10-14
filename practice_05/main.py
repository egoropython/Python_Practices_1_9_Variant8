from functools import reduce

orders = [
    {"number": 101, "customer": "Иванов", "cost": 1500.0, "status": "новый"},
    {"number": 102, "customer": "Петров", "cost": 750.0, "status": "отменён"},
    {"number": 103, "customer": "Иванов", "cost": 3200.0, "status": "оплачен"},
    {"number": 104, "customer": "Сидоров", "cost": 2100.0, "status": "отправлен"},
]

def active_orders(items):
    return list(filter(lambda order: order["status"] != "отменён", items))

def order_numbers(items):
    return list(map(lambda order: order["number"], items))

def sort_by_cost(items):
    return sorted(items, key=lambda order: order["cost"])

def total_cost(items):
    return reduce(lambda total, order: total + order["cost"], items, 0.0)

def has_cancelled(items):
    return any(order["status"] == "отменён" for order in items)

def orders_for_customer(items, customer):
    """Лениво возвращает заказы выбранного клиента."""
    for order in items:
        if order["customer"].casefold() == customer.casefold():
            yield order

def main():
    print("Активные заказы:", active_orders(orders))
    print("Номера заказов:", order_numbers(orders))
    print("Сортировка по стоимости:", sort_by_cost(orders))
    print(f"Общая стоимость: {total_cost(orders):.2f} руб.")
    print("Есть отменённые заказы:", "да" if has_cancelled(orders) else "нет")
    customer = input("Введите клиента для генератора (Иванов/Петров/Сидоров): ").strip()
    print("Заказы клиента:")
    for order in orders_for_customer(orders, customer): print(order)

if __name__ == "__main__": main()
