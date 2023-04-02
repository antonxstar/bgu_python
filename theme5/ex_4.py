# сортировка списка
x = [-3,5,1,0,1,2,-3]
print(sorted(x))
print(sorted([-3,5,1,0,1,2,-3]))
# сортировка в обратном порядке
print(sorted(x, reverse=True))
words = ['здесь','нужно','руками','кидать','воду','вверх']
print(sorted(words))
# сортировка по алфавитному порядку вне зависимости от регистра букв
print(sorted(words, key=str.lower))
#  сортировка списка с его изменением
words.sort(key=str.lower)
print(words)
y = [2,3,-1,7,-2,-2,1]
# генерация нового списка на основе ранее созданных
coords = [(x[i],y[i]) for i in range(7)]
print(coords)
print(sorted(coords))
print(sorted(coords, reverse=True))
print(sorted(coords, key=lambda coord:(-coord[0], coords[1])))