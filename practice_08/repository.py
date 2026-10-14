class MembershipRepository:
    def __init__(self): self._items={}
    def add(self,membership): self._items[membership.membership_id]=membership
    def get(self,membership_id): return self._items.get(membership_id)
    def get_all(self): return list(self._items.values())
    def delete(self,membership_id): return self._items.pop(membership_id,None)
