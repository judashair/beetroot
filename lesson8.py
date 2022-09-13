# task 1
def favorite_movie(name):
    print(f"My favorite movie is '{name}'.")

favorite_movie("Harry Potter")

# task 2
def make_country(capital, name):
    country_dict = {'country_name': name, 'capital': capital}
    return country_dict

print(make_country("Warsaw", "Poland"))

# task 3
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
    return print(x)

make_operation("+", 7, 12, 2)
make_operation("-", 5, 45, -10, -20,)
make_operation("*", 6, 9)
