def make_operation(symbol, *args):
    x = 0
    if symbol == "+":
        for numbers in args:
            x += numbers
    elif symbol == "-":
        for numbers in args:
            x -= numbers
    elif symbol == "*":
        x = 1
        for numbers in args:
            x *= numbers
    return x