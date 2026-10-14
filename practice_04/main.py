from storage import JsonStorage
from service import OrderService
from exceptions import OrderNotFoundError

def main():
    service = OrderService(JsonStorage())
    while True:
        print("\n=== Управление заказами ===")
        print("1. Создать заказ  2. Все заказы  3. Найти заказ  4. Изменить статус  5. Отменить  0. Выход")
        choice = input("Выберите пункт: ").strip()
        try:
            if choice == "1":
                customer = input("Клиент: ").strip()
                name = input("Товар: ").strip()
                price = float(input("Цена: ")); quantity = int(input("Количество: "))
                print("Создан:", service.create(customer, [{"name": name, "price": price, "quantity": quantity}]))
            elif choice == "2":
                for order in service.all_orders(): print(order)
            elif choice == "3": print(service.search(int(input("Номер заказа: "))))
            elif choice == "4": print(service.change_status(int(input("Номер заказа: ")), input("Новый статус: ").strip()))
            elif choice == "5": print(service.cancel(int(input("Номер заказа: "))))
            elif choice == "0": break
            else: print("Неизвестный пункт меню.")
        except (ValueError, OrderNotFoundError) as exc: print(f"Ошибка: {exc}")

if __name__ == "__main__": main()
