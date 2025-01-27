from functools import wraps

def handle_api_error(func):
    """
    A decorator to handle errors in API requests.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error in {func.__name__}: {e}")
            return []
    return wrapper