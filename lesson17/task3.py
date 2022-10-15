class Fraction:

    def __init__(self, numerator: int, denominator: int):
        self.denominator = denominator
        self.numerator = numerator

        if self.numerator == 0 or self.denominator == 0:
            raise ValueError("Numerator and denominator have to be not a zero")

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

    def reduction(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        a = 0
        while a < 5:
            for i in range(2, 10):
                if self.numerator % i == 0 and self.denominator % i == 0:
                    self.numerator = int(self.numerator / i)
                    self.denominator = int(self.denominator / i)
                continue
            a += 1
        return f'{self.numerator}/{self.denominator}'

    def __add__(self, other):
        self.numerator = self.numerator * other.denominator + other.numerator * self.denominator
        self.denominator = self.denominator * other.denominator
        self.reduction(self.numerator, self.denominator)
        return f'{self.numerator}/{self.denominator}'

    def __sub__(self, other):
        self.numerator = self.numerator * other.denominator - other.numerator * self.denominator
        self.denominator = self.denominator * other.denominator
        self.reduction(self.numerator, self.denominator)
        return f'{self.numerator}/{self.denominator}'

    def __mul__(self, other):
        self.numerator = self.numerator * other.numerator
        self.denominator = self.denominator * other.denominator
        self.reduction(self.numerator, self.denominator)
        return f'{self.numerator}/{self.denominator}'

    def __truediv__(self, other):
        self.numerator = self.numerator * other.denominator
        self.denominator = self.denominator * other.numerator
        self.reduction(self.numerator, self.denominator)
        return f'{self.numerator}/{self.denominator}'


f1 = Fraction(1, 2)
f2 = Fraction(1, 4)
print(f1 + f2)
print(f1 - f2)
print(f1 * f2)
print(f1 / f2)
