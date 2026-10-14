class InMemoryClientRepository:
    def __init__(self): self._items = {}
    def add(self, client): self._items[client.client_id] = client
    def get(self, client_id): return self._items.get(client_id)
    def get_all(self): return list(self._items.values())
    def delete(self, client_id): return self._items.pop(client_id, None)
