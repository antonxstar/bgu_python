stroka = input()       # считал строку
stroka = stroka.split(' ')           # создать список из строки, в качестве разделителя задан пробел

for idx in range(len(stroka)):       # итерируюсь по списку
    if stroka[idx][0].isupper():       # делаю проверку на большую букву в каждом элементе списка
        stroka[idx] = stroka[idx][0].lower() + stroka[idx][1:]   # заменяю элемент списка на другой элемент где буква первая не заглавная
        #print(stroka[idx][0].lower())

stroka = ' '.join(stroka)   # беру список и соединяю элементы списка в строку через пробел
print(stroka)

