import re
#https://docs.python.org/3/library/re.html
regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"


class Mail:

    def __init__(self, email):
        self.email = email

    @property
    def validate(self):
        if re.search(regex, self.email):
            return self.email
        else:
            return "Invalid e-mail."


a = Mail("abc.def@mail.com")
b = Mail("abc..@mail.com")
c = Mail("abc_def@mail.com")


print(a.validate)
print(b.validate)
print(c.validate)
