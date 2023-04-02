x = int(input('Введите два целых числа. Первое: '))
y = int(input('Второе: '))
for i in range(x,y):
    if i % 10 == 0:
        print('%d делится на 10' % i)
        break
else:
    print('ни одно из чисел не делится на 10')