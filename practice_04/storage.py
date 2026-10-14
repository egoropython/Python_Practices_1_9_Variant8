import json
from pathlib import Path

class JsonStorage:
    def __init__(self, path="orders.json"):
        self.path = Path(path)

    def load(self):
        if not self.path.exists(): return []
        try:
            with self.path.open("r", encoding="utf-8") as file:
                data = json.load(file)
            if not isinstance(data, list): raise ValueError("Корневое значение JSON должно быть списком.")
            return data
        except json.JSONDecodeError as exc:
            raise ValueError(f"Файл JSON повреждён: {exc}") from exc

    def save(self, orders):
        with self.path.open("w", encoding="utf-8") as file:
            json.dump(orders, file, ensure_ascii=False, indent=2)
