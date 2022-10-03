def logger(func):
    def deco_print(*args, **kwargs):
        return (f"Тут {func.__name__} функція та її аргументи {*args, *kwargs}")
    return deco_print


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


print(add(4, 5))
print(square_all(4, 5))
