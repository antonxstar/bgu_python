stroka = input()       # считал строку
stroka = stroka.split(' ')           # создать список из строки, в качестве разделителя задан пробел
count = 0
for idx in range(len(stroka)):       # итерируюсь по списку
    if stroka[idx].isdigit():       # делаю проверку на число в каждом элементе списка
        count += int(stroka[idx])   # считаю числа

print(count)
