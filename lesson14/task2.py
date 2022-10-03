from functools import wraps


def stop_words(words: list):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            new_string = func(*args, **kwargs)
            for word in words:
                new_string = new_string.replace(word, '*')
            return new_string

        return inner

    return wrapper


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str):
    return f"{name} drinks pepsi in his brand new BMW!"


print(create_slogan('Anna'))
assert create_slogan("Steve") == "Steve drinks * in his brand new *!"

