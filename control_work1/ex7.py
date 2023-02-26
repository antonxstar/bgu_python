# Дано:
# n рублей
# поход в кино стоит k рублей
# пирожок стоит p рублей
# Найти:
# сможет ли Петя сходить в кино?
# сможет ли Петя купить пирожок?
# и то, и другое сразу?
# Решение:
n = int(input('Денег у Пети:'))          # вводд данных
k = int(input('Стоимость кино:'))
p = int(input('Стоимость пирожка:'))
s1 = n - k                               # сколько у него останется после покупки билета в кино
s2 = n - p                               # сколько у него останется после покупки пирожка
s3 = n - k - p                           # сколько у него останется после покупки билета в кино и пирожка
if s1 >= 0:                              # если после покупки билета в кино у него останется больше либо равно 0, то
    print('Петя сможет сходить в кино')  # выводим что петя сможет сходить в кино
if s2 >= 0:                              # если после покупки пирожка у него останется больше либо равно 0, то
    print('Петя сможет купить пирожок')  # выводим что петя сможет купить пирожок
if s3 >= 0:                              # если после покупки и пирожка и билета в кино у него останется больше либо равно 0, то
    print('Петя сможет и сходить в кино и купить пирожок')  # выводим что петя сможет купить и пирожок и билет в кино