from functools import wraps


class TypeDecorators:

    @classmethod
    def to_(cls, type_):
        def transform(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                func(*args, **kwargs)
                try:
                    value = type_(*args, **kwargs)
                    print(value, type(value))
                except ValueError:
                    print(f"It's not possible to convert the result into {type_}!")
            return wrapper
        return transform


@TypeDecorators.to_(int)
def do_nothing(string):
    return string


@TypeDecorators.to_(bool)
def do_something(string):
    return string


try:
    do_nothing("25")
    do_something("True")
except NameError as error_msg:
    print(error_msg)
except TypeError as error_msg:
    print(error_msg)
