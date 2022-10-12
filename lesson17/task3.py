class Fraction:

    def __init__(self, numerator: int, denominator: int):
        self.den = denominator
        self.num = numerator

    def __add__(self, other):
        return Fraction(self.num * other.den + self.den * other.num, self.den * other.den)

    def __sub__(self, other):
        return Fraction(self.num * other.den - other.num * self.den, self.den * other.den)
        pass

    def __truediv__(self, other):
        return self.__mul__(Fraction(other.den, other.num))

    def __mul__(self, other):
        return Fraction(self.num * other.num, self.den * other.den)

    def __str__(self):
        return f"{self.num}\n——\n{self.den}\n"

# if __name__ == '__main__':
f1 = Fraction(1, 2)
f2 = Fraction(1, 4)
print(f1 + f2)
print(f1 - f2)
print(f1 * f2)
print(f1 / f2)
