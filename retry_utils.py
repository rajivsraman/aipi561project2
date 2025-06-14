import time
import functools

def retry(max_retries=2, delay=2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_retries:
                        raise
                    print(f"Retry {attempt+1}/{max_retries} after error: {e}")
                    time.sleep(delay)
        return wrapper
    return decorator