# импорт модуля в котором определена функция itemgetter
import operator
name_and_age = [('Andrews, R.', 23), ('MacArthur, M.', 52), ('Coleman, T.', 32), ('Cummings, J.', 23), ('Zimmerman, A.', 29),]
# вначале производится сортировка по менее приоритетному компоненту
name_and_age.sort(key=operator.itemgetter(0))
print(name_and_age)
# затем по более приоритетному
name_and_age.sort(key=operator.itemgetter(1), reverse=True)
print(name_and_age)