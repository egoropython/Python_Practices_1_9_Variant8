from repositories import InMemoryClientRepository
from notifications import ConsoleNotifier
from pricing import StandardPricing, DiscountPricing, FamilyPricing
from services import FitnessService

def main():
    repository=InMemoryClientRepository(); notifier=ConsoleNotifier(); pricing=StandardPricing()
    service=FitnessService(repository,notifier,pricing)
    while True:
        print("\n=== Фитнес-центр (SOLID) ===")
        print("1. Регистрация клиента  2. Оформить абонемент  3. Запись на тренировку")
        print("4. Отменить запись  5. Список клиентов  6. Сменить тариф  0. Выход")
        choice=input("Выберите пункт: ").strip()
        try:
            if choice=="1": print(service.register_client(input("Имя: "),int(input("Возраст: "))))
            elif choice=="2": print(service.create_membership(int(input("ID клиента: ")),input("Тип (разовый/месячный/годовой): ").strip()))
            elif choice=="3": print(service.book_training(int(input("ID клиента: ")),int(input("ID тренера: ")),input("Время: ").strip()))
            elif choice=="4": print(service.cancel_booking(int(input("ID записи: "))))
            elif choice=="5":
                for client in repository.get_all(): print(client)
            elif choice=="6":
                print("1. Стандартный 2. Скидка 3. Семейный")
                t=input("Тариф: ").strip(); service.pricing={"1":StandardPricing(),"2":DiscountPricing(),"3":FamilyPricing()}[t]; print("Тариф изменён.")
            elif choice=="0": break
            else: print("Неизвестный пункт меню.")
        except (ValueError,KeyError) as exc: print("Ошибка:",exc)
if __name__=="__main__": main()
