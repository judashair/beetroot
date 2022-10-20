from functools import wraps


class TypeDecorators:
    error_message = "Impossible to convert."

    def __init__(self, func):
        self.func = func

    @classmethod
    def to_int(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = int(func(*args, **kwargs))
                return result
            except Exception:
                raise Exception(cls.error_message)

        return wrapper

    @classmethod
    def to_float(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = float(func(*args, **kwargs))
                return result
            except Exception:
                raise Exception(cls.error_message)

        return wrapper

    @classmethod
    def to_bool(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = bool(func(*args, **kwargs))
                return result
            except Exception:
                raise Exception(cls.error_message)

        return wrapper

    @classmethod
    def to_str(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = str(func(*args, **kwargs))
                return result
            except Exception:
                raise Exception(cls.error_message)

        return wrapper


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


@TypeDecorators.to_float
def do_something_else(string: str):
    return string


@TypeDecorators.to_str
def do_something_new(string):
    return string


print(do_nothing("25"))
print(do_something(""))
print(do_something_else("5"))
print(do_something_new([1, 2, 3]))


