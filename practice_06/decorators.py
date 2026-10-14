from functools import wraps
from time import perf_counter

def log_call(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"[LOG] вызов {function.__name__}")
        result = function(*args, **kwargs)
        print(f"[LOG] {function.__name__} завершена")
        return result
    return wrapper

def limit_calls(max_calls):
    def decorator(function):
        calls = 0
        @wraps(function)
        def wrapper(*args, **kwargs):
            nonlocal calls
            if calls >= max_calls: raise RuntimeError("Лимит вызовов исчерпан.")
            calls += 1
            return function(*args, **kwargs)
        return wrapper
    return decorator

def measure_time(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        try: return function(*args, **kwargs)
        finally: print(f"[TIME] {function.__name__}: {perf_counter()-start:.6f} сек.")
    return wrapper
