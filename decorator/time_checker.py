import time
from datetime import timedelta
from miauc.service import Service


def time_check_notifier(title:str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            Service.to().send_message(f'{title} 시작')
            start = time.time()
            result = func(*args, **kwargs)
            end = timedelta(seconds=(time.time() - start))
            Service.to().send_message(f'{title} 종료({end})')
            return result
        return wrapper
    return decorator