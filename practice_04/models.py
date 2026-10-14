from dataclasses import dataclass, asdict

@dataclass
class Order:
    number: int
    customer: str
    items: list
    status: str = "новый"

    @property
    def total(self):
        return round(sum(float(item["price"]) * int(item["quantity"]) for item in self.items), 2)

    def to_dict(self):
        data = asdict(self); data["total"] = self.total; return data
