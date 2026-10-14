from models import Membership
class MembershipFactory:
    PRICES={"разовый":500.0,"месячный":2500.0,"годовой":24000.0}
    @classmethod
    def create(cls,membership_id,client_name,kind,months=1):
        if kind not in cls.PRICES: raise ValueError("Неизвестный тип абонемента.")
        if months <= 0: raise ValueError("Количество месяцев должно быть положительным.")
        return Membership(membership_id,client_name,kind,months,cls.PRICES[kind])
