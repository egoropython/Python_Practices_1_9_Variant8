from dataclasses import dataclass
from enum import Enum

class MembershipStatus(Enum):
    ACTIVE = "активен"
    EXPIRED = "истёк"
    FROZEN = "заморожен"
    CANCELLED = "отменён"

@dataclass
class Client:
    client_id: int
    name: str
    age: int
    visits: int = 0

    def get_report_data(self):
        return {"id": self.client_id, "name": self.name, "visits": self.visits}

@dataclass
class Trainer:
    trainer_id: int
    name: str
    specialization: str

@dataclass
class Membership:
    membership_id: int
    client_id: int
    months: int
    price: float
    status: MembershipStatus = MembershipStatus.ACTIVE

    def get_report_data(self):
        return {"id": self.membership_id, "client_id": self.client_id, "status": self.status.value}
