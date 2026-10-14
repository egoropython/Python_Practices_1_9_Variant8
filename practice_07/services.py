from models import Client, Membership, TrainingBooking, MembershipStatus
class FitnessService:
    """Бизнес-логика зависит от абстракций репозитория, тарифа и уведомителя."""
    def __init__(self, repository, notifier, pricing):
        self.repository=repository; self.notifier=notifier; self.pricing=pricing
        self.memberships={}; self.bookings={}; self._next_client=1; self._next_membership=1; self._next_booking=1
    def register_client(self,name,age):
        if not name.strip() or age < 14: raise ValueError("Укажите имя; возраст от 14 лет.")
        client=Client(self._next_client,name.strip(),age); self._next_client+=1
        self.repository.add(client); self.notifier.send(f"Клиент {client.name} зарегистрирован")
        return client
    def create_membership(self,client_id,kind,months=1):
        if self.repository.get(client_id) is None: raise KeyError("Клиент не найден.")
        price=self.pricing.calculate(kind,months)
        membership=Membership(self._next_membership,client_id,kind,price); self._next_membership+=1
        self.memberships[membership.membership_id]=membership
        self.notifier.send(f"Оформлен абонемент №{membership.membership_id}")
        return membership
    def book_training(self,client_id,trainer_id,time):
        if self.repository.get(client_id) is None: raise KeyError("Клиент не найден.")
        booking=TrainingBooking(self._next_booking,client_id,trainer_id,time); self._next_booking+=1
        self.bookings[booking.booking_id]=booking; self.notifier.send(f"Запись на тренировку №{booking.booking_id} создана")
        return booking
    def cancel_booking(self,booking_id):
        booking=self.bookings.pop(booking_id,None)
        if booking is None: raise KeyError("Запись не найдена.")
        self.notifier.send(f"Запись №{booking_id} отменена"); return booking
