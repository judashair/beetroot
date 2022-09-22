#task1
def kwadrat_div():
    a = input('Enter number a: ')
    b = input('Enter number b: ')

    try:
        int(a)**2/int(b)
    except ValueError:
        print('Your input is not digit!')
    except ZeroDivisionError:
        print("You try to divide by zero! Enter the other value of 'b'!")
    else:
        return print('The answer is: ' + str(int(a)**2/int(b)))


kwadrat_div()

#task2
def oops_index_error():
    raise IndexError


def oops_key_error():
    raise KeyError


def another_function():
    names = {'Lviv': 1, "Warsaw": 2}
    try:
        print(names['Berlin'])
        print("No IndexErrors")
    except:
        oops_index_error()


another_function()
