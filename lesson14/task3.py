from functools import wraps


def arg_rules(type_: type, max_length: int, contains: list):
    def inner(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            if not type(*args, **kwargs) == type_:
                print(f"The type of slogan must be {type_} - given {type(*args, **kwargs)}")
                return False
            if not max_length >= len(*args, **kwargs):
                print(f"The len of the input must be {max_length} max - given {len(*args, **kwargs)}")
                return False
            for i in contains:
                if i not in str(*args, **kwargs):
                    print(f"The name must contain {contains} - given {str(*args, **kwargs)}")
                    return False
            return func(*args, **kwargs)
        return wrap
    return inner


@arg_rules(type_=str, max_length=15, contains=["05", "@"])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


print(create_slogan("johndoe05@gmail.com"))
print(create_slogan("S@SH05"))
print(create_slogan(15))
print(create_slogan("python"))
