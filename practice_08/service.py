from factory import MembershipFactory
from repository import MembershipRepository
class MembershipService:
    def __init__(self,repository,strategy,observers=None):
        self.repository=repository; self.strategy=strategy; self.observers=list(observers or []); self._next_id=1
    def _notify(self,event,membership):
        for observer in self.observers: observer.update(event,membership)
    def create(self,client_name,kind,months=1):
        if not client_name.strip(): raise ValueError("Имя клиента не должно быть пустым.")
        membership=MembershipFactory.create(self._next_id,client_name.strip(),kind,months); self._next_id+=1
        membership.price=round(self.strategy.calculate(membership),2)
        self.repository.add(membership); self._notify("создан",membership); return membership
    def cancel(self,membership_id):
        membership=self.repository.get(membership_id)
        if membership is None: raise KeyError("Абонемент не найден.")
        self.repository.delete(membership_id); self._notify("удалён",membership); return membership
    def set_strategy(self,strategy): self.strategy=strategy
