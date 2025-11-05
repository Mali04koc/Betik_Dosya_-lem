from functools import wraps
import time

def timer(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        t0= time.perf_counter() # 0.andaki time
        result=func(*args,**kwargs)
        total_time=time.perf_counter()-t0
        print("total_time: ", total_time)
        return result
    return wrapper


def required_columns(requireds: set[str]):
    """Decorate a function expecting `rows: list[dict]` as first arg and validate schema."""
    def deco(func):
        @wraps(func)
        def wrapper(rows, *args, **kwargs):
            if not rows:
                raise ValueError("Boş veri seti")
            first = rows[0]
            if not isinstance(first, dict):
                raise TypeError("Beklenen satır türü dict olmalı")
            keys = set(first.keys())
            missing = requireds - keys
            if missing:
                raise ValueError(f"Eksik kolon(lar): {', '.join(sorted(missing))}")
            return func(rows, *args, **kwargs)
        return wrapper
    return deco
        
                


