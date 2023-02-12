d = (input('Введите количество фишек у Димы: '))
v = (input('Введите количество фишек у Вовы: '))
if d == v:
    print('У мальчиков одинаковое количество фишек')
else:
    first_boy = 'Димы' if d > v else 'Вовы'
    second_boy = 'Вовы' if d > v else 'Димы'
    print('У %s больше фишек, чем у %s.' % (first_boy,second_boy))