from service import FitnessService

def main():
    service = FitnessService()
    while True:
        print("\n=== Фитнес-центр ===")
        print("1. Добавить клиента  2. Удалить клиента  3. Найти клиента")
        print("4. Все клиенты  5. Изменить статус абонемента  6. Отметить посещение")
        print("7. Посещаемость  8. Интроспекция клиента  0. Выход")
        choice = input("Выберите пункт: ").strip()
        try:
            if choice == "1":
                client = service.add_client(input("Имя: "), int(input("Возраст: "))); print(client)
            elif choice == "2":
                cid=int(input("ID клиента: "))
                if cid not in service.clients: raise KeyError("Клиент не найден.")
                del service.clients[cid]; print("Клиент удалён.")
            elif choice == "3": print(service.clients.get(int(input("ID клиента: ")), "Клиент не найден."))
            elif choice == "4":
                for client in service.clients.values(): print(client)
            elif choice == "5": print(service.set_membership_status(int(input("ID абонемента: ")), input("Статус (активен/истёк/заморожен/отменён): ").strip()))
            elif choice == "6": print(service.record_visit(int(input("ID клиента: "))))
            elif choice == "7": print("Всего посещений:", service.attendance())
            elif choice == "8": service.inspect_client(int(input("ID клиента: ")))
            elif choice == "0": break
            else: print("Неизвестный пункт меню.")
        except (ValueError, KeyError, RuntimeError) as exc: print("Ошибка:", exc)

if __name__ == "__main__": main()
