from repository import MembershipRepository
from observers import ConsoleObserver,HistoryObserver
from strategies import StandardStrategy,DiscountStrategy,FamilyStrategy
from service import MembershipService

def main():
    history=HistoryObserver(); service=MembershipService(MembershipRepository(),StandardStrategy(),[ConsoleObserver(),history])
    while True:
        print("\n=== Абонементы фитнес-центра ===")
        print("1. Создать абонемент  2. Показать все  3. Удалить абонемент")
        print("4. Выбрать стратегию цены  5. История событий  0. Выход")
        choice=input("Выберите пункт: ").strip()
        try:
            if choice=="1": print(service.create(input("Клиент: "),input("Тип (разовый/месячный/годовой): ").strip(),int(input("Месяцев: "))))
            elif choice=="2":
                for item in service.repository.get_all(): print(item)
            elif choice=="3": print(service.cancel(int(input("ID абонемента: "))))
            elif choice=="4":
                print("1. Стандартная 2. Скидка 3. Семейная")
                service.set_strategy({"1":StandardStrategy(),"2":DiscountStrategy(),"3":FamilyStrategy()}[input("Стратегия: ").strip()]); print("Стратегия изменена.")
            elif choice=="5": print(history.events)
            elif choice=="0": break
            else: print("Неизвестный пункт меню.")
        except (ValueError,KeyError) as exc: print("Ошибка:",exc)
if __name__=="__main__": main()
