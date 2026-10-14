from models import Client, Trainer, Membership, MembershipStatus
from decorators import log_call, limit_calls, measure_time
from context import operation_log

class FitnessService:
    def __init__(self):
        self.clients = {1: Client(1, "Анна", 21, 12), 2: Client(2, "Иван", 25, 8)}
        self.trainers = {1: Trainer(1, "Олег", "силовые тренировки")}
        self.memberships = {1: Membership(1, 1, 1, 2500), 2: Membership(2, 2, 12, 22000)}

    @log_call
    @measure_time
    @limit_calls(20)
    def add_client(self, name, age):
        if not name.strip() or age < 14: raise ValueError("Имя обязательно, возраст должен быть не меньше 14 лет.")
        new_id = max(self.clients, default=0) + 1
        self.clients[new_id] = Client(new_id, name.strip(), age)
        return self.clients[new_id]

    def set_membership_status(self, membership_id, status):
        if membership_id not in self.memberships: raise KeyError("Абонемент не найден.")
        if status not in {s.value for s in MembershipStatus}: raise ValueError("Неизвестный статус.")
        membership = self.memberships[membership_id]
        membership.status = next(s for s in MembershipStatus if s.value == status)
        return membership

    def record_visit(self, client_id):
        if client_id not in self.clients: raise KeyError("Клиент не найден.")
        with operation_log(operation=f"посещение клиента {client_id}"):
            self.clients[client_id].visits += 1
        return self.clients[client_id]

    def attendance(self):
        return sum(c.visits for c in self.clients.values())

    def inspect_client(self, client_id):
        if client_id not in self.clients: raise KeyError("Клиент не найден.")
        obj = self.clients[client_id]
        print("Тип:", type(obj).__name__)
        print("Является Client:", isinstance(obj, Client))
        print("Есть visits:", hasattr(obj, "visits"))
        print("Имя через getattr:", getattr(obj, "name", "не указано"))
        print("Атрибуты:", ", ".join(name for name in dir(obj) if not name.startswith("__")))
        return obj
