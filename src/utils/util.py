
def try_except_handling(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print("error", e)
            return None
    return wrapper


def merge_dicts(a, b):
    c = a.copy()
    c.update(b)
    return c