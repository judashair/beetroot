def fullname(firstname, lastname):
    return f"{firstname} {lastname}"


def greeting(function):
    def invitation(fr_name, la_name):
        fr_name = str(input("Enter your first name: ").title())
        la_name = str(input("Enter your last name: ").title())
        return f"Good morning, {function(fr_name, la_name)}! Wish you a good day."

    return invitation


my_name = greeting(fullname)
print(my_name(fr_name=str, la_name=str))



