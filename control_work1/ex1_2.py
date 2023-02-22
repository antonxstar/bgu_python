a = float(input("Введите a : ")) # Вводим число a
b = float(input("Введите b : ")) # Вводим число b
if a>b:
   c = (b/a)*100
   cr = round(c, 2)
   print(cr)
if a<b:
   c = (a/b)*100
   cr = round(c, 2)
   print(cr)