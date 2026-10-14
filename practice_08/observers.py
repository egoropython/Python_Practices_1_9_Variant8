class MembershipObserver:
    def update(self,event,membership): raise NotImplementedError
class ConsoleObserver(MembershipObserver):
    def update(self,event,membership): print(f"[СОБЫТИЕ] {event}: абонемент №{membership.membership_id}, {membership.client_name}")
class HistoryObserver(MembershipObserver):
    def __init__(self): self.events=[]
    def update(self,event,membership): self.events.append({"event":event,"id":membership.membership_id,"client":membership.client_name})
