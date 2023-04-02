n = int(input('Введите длину списка: '))
x = 0
surnames = []

while x <= n-1:
    surnames.append(input('Введите фамилию: '))
    x += 1

surnames = sorted(surnames, key=str.lower)

for x in range(len(surnames)):
    print(x+1, surnames[x])