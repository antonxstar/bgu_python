surname_1 = 'Паховцев'
surname_2 = 'Епифанцев'
sport = 'шашки'
# вставка аргументов метода format в места, указанные фигурными скобками, по порядку
print('{} и {} играют в {}'.format(surname_1, surname_2, sport))
# в скобках можно указывать, какой по счёту аргумент следует сюда вставить
print('{1} и {0} играют в {2}'.format(surname_1, surname_2, sport))
points_1 = 1
points_2 = 2
print('Счёт {:d}:{:d} в пользу {}a'.format(points_1,points_2,surname_1))
print('Счёт {1:d}:{0:d} в пользу {2}a'.format(points_1,points_2,surname_1))