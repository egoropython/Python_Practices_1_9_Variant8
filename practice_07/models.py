from dataclasses import dataclass
from enum import Enum
class MembershipStatus(Enum): ACTIVE="активен"; EXPIRED="истёк"; FROZEN="заморожен"; CANCELLED="отменён"
@dataclass
class Client:
    client_id:int; name:str; age:int
@dataclass
class Trainer:
    trainer_id:int; name:str; specialization:str
@dataclass
class Membership:
    membership_id:int; client_id:int; kind:str; price:float; status:MembershipStatus=MembershipStatus.ACTIVE
@dataclass
class TrainingBooking:
    booking_id:int; client_id:int; trainer_id:int; time:str
