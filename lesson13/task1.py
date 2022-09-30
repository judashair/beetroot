def first():
    a = 1
    b = 2
    c = "morning"
    line = "python"


def sqrt_numbers(*args):
    return list(map(lambda x: x ** 2, args))


def another():
    slovo = "slovo"
    return "slovo"


def count_locals(func):
    return f'Number of local variables in function {func.__name__}: {func.__code__.co_nlocals}'


print(count_locals(first))
print(count_locals(sqrt_numbers))
print(count_locals(another))
