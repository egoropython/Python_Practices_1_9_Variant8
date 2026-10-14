from dataclasses import dataclass
from enum import Enum
class MembershipStatus(Enum): ACTIVE="активен"; EXPIRED="истёк"; FROZEN="заморожен"; CANCELLED="отменён"
@dataclass
class Membership:
    membership_id:int
    client_name:str
    kind:str
    months:int
    price:float
    status:MembershipStatus=MembershipStatus.ACTIVE
