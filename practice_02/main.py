accounts = [
    {"number": "40801", "owner": "Иванов И.И.", "type": "текущий", "balance": 12500.0},
    {"number": "40802", "owner": "Петров П.П.", "type": "накопительный", "balance": 48000.0},
    {"number": "40803", "owner": "Иванов И.И.", "type": "накопительный", "balance": 27500.0},
]


def find_by_owner(items, owner):
    return [account for account in items if account["owner"].casefold() == owner.casefold()]


def filter_by_type(items, account_type):
    return [account for account in items if account["type"].casefold() == account_type.casefold()]


def total_balance(items):
    return sum(account["balance"] for account in items)


def sort_by_balance(items):
    return sorted(items, key=lambda account: account["balance"], reverse=True)


def show_accounts(items):
    if not items:
        print("Счета не найдены.")
        return
    for account in items:
        print(f"№ {account['number']} | {account['owner']} | {account['type']} | {account['balance']:.2f} руб.")


def main():
    while True:
        print("\n=== Банковские счета ===")
        print("1. Все счета  2. По владельцу  3. По типу  4. Сортировка по балансу")
        print("5. Общий баланс  6. Максимальный баланс  7. Уникальные типы  0. Выход")
        choice = input("Выберите пункт: ").strip()
        if choice == "1": show_accounts(accounts)
        elif choice == "2": show_accounts(find_by_owner(accounts, input("Владелец: ").strip()))
        elif choice == "3": show_accounts(filter_by_type(accounts, input("Тип счёта: ").strip()))
        elif choice == "4": show_accounts(sort_by_balance(accounts))
        elif choice == "5": print(f"Общий баланс: {total_balance(accounts):.2f} руб.")
        elif choice == "6": print("Максимальный баланс:"); show_accounts(sort_by_balance(accounts)[:1])
        elif choice == "7": print("Типы счетов:", ", ".join(sorted({a['type'] for a in accounts})))
        elif choice == "0": break
        else: print("Неизвестный пункт меню.")

if __name__ == "__main__": main()
