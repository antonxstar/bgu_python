# Дано:
# 4 введённых числа
# Найти:
# максимальное число = ?
# Решение:
a = float(input('Введите первое число:'))                   # 1.1.вводим 1 - ое число
b = float(input('Введите второе число:'))                   # 1.2.вводим 2 - ое число
c = float(input('Введите третье число:'))                   # 1.3.вводим 3 - е число
d = float(input('Введите четвёртое число:'))                # 1.4.вводим 4 - ое число
if (a > b) and (a > c) and (a > d):                         # 2.1.если a больше b, c и d, то
    print('самое большое число: ',a)                        # вывести a
if (b > a) and (b > c) and (b > d):                         # 2.2.если b больше a, c и d, то
    print('самое большое число: ',b)                        # вывести b
if (c > a) and (c > b) and (c > d):                         # 2.3.если с больше a, b и d, то
    print('самое большое число: ',c)                        # вывести c
if (d > a) and (d > b) and (d > c):                         # 2.4.если d больше a, b и c, то
    print('самое большое число: ',d)                        # вывести d
