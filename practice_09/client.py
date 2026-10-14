import socket, json
from protocol import encode_message
HOST="127.0.0.1"; PORT=50508
def request(command,data=None):
    with socket.create_connection((HOST,PORT),timeout=5) as sock:
        sock.sendall(encode_message({"command":command,"data":data or {}}))
        line=sock.makefile("rb").readline()
        if not line: raise ConnectionError("Сервер закрыл соединение без ответа")
        return json.loads(line.decode("utf-8"))
def main():
    while True:
        print("\n=== Кинотеатр: каталог фильмов ===")
        print("1. Все фильмы  2. Фильм по ID  3. Добавить фильм")
        print("4. Изменить фильм  5. Удалить фильм  6. Поиск по жанру  0. Выход")
        choice=input("Выберите пункт: " ).strip()
        try:
            if choice=="1": result=request("list")
            elif choice=="2": result=request("get",{"id":int(input("ID фильма: "))})
            elif choice=="3": result=request("create",{"title":input("Название: "),"genre":input("Жанр: "),"duration_minutes":int(input("Длительность в минутах: ")),"age_rating":int(input("Возрастной рейтинг: "))})
            elif choice=="4": result=request("update",{"id":int(input("ID фильма: ")),"title":input("Новое название (Enter — без изменений): "),"genre":input("Новый жанр (Enter — без изменений): " )})
            elif choice=="5": result=request("delete",{"id":int(input("ID фильма: "))})
            elif choice=="6": result=request("by_genre",{"genre":input("Жанр: " )})
            elif choice=="0": break
            else: print("Неизвестный пункт меню."); continue
            print(json.dumps(result,ensure_ascii=False,indent=2))
        except (ValueError,OSError,ConnectionError) as exc: print("Ошибка:",exc)
if __name__=="__main__": main()
