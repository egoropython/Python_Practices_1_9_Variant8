from contextlib import contextmanager
from datetime import datetime
from pathlib import Path

@contextmanager
def operation_log(path="operations.log", operation="операция"):
    started = datetime.now()
    try:
        yield
    except Exception as exc:
        with Path(path).open("a", encoding="utf-8") as file:
            file.write(f"{started.isoformat()} | {operation} | ошибка: {exc}\n")
        raise
    else:
        with Path(path).open("a", encoding="utf-8") as file:
            file.write(f"{started.isoformat()} | {operation} | успешно\n")
