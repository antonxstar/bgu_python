ost = 25      # осталось спичек
print('на столе лежат 25 спичек. За один раз каждый игрок может взять от 1 до 4 спичек. Победит тот кто возьмёт последнюю')
player = 1           # какой игрок делает ход
while ost != 0:
    print('Игрок',player,'делает ход:')
    if ost>0:
        b = int(input('Введите сколько вы хотите взять спичек со стола: '))
        if b == 1 or b == 2 or b == 3 or b == 4:
            if ost - b >= 0:
                ost -= b
                print('вы взяли ', b, 'спичек.' + ' На столе осталось', ost, 'спичек')
                if player == 1:
                    player += 1
                else:
                    player -= 1
            else:
                print('на столе осталось всего',ost,'спички, возьмите меньше')
        else:
            print('можно взять либо 1 либо 2 либо 3 либо 4')
if ost == 0:
    if player == 1:
        player += 1
    else:
        player -= 1
print('Игрок',player,'взял последнюю спичку')
print('Игрок',player,'победил!')