n = 1.2
print(n.__int__())

class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def meow(self):
        print(f"{self.name} says 'Meow!'")


my_cat = Cat("Мурка", "белая")
my_cat2 = Cat("Мурзик", "черный")
my_cat.meow()

print(my_cat2.name)
print(my_cat2.color)
my_cat2.meow()

print(type(my_cat))
print(type(n))

x = 20
print(bin(x))
print(hex(x))
print(oct(x))

print(.1+.1+.1+.1+.1+.1+.1+.1+.1+.1+.1)

from decimal import *
getcontext().prec = 6
print(Decimal(.1)+Decimal(.1)+Decimal(.1)+Decimal(.1)+Decimal(.1)+
      Decimal(.1)+Decimal(.1)+Decimal(.1)+Decimal(.1)+Decimal(.1)+Decimal(.1))

from fractions import Fraction
print(Fraction(1, 3))

print(1/3)
