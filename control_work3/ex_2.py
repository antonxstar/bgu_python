n = int(input('n='))
x = 0
cities = []

while x <= n-1:
    cities.append(input())
    x += 1

new_сities = cities.copy()

for e in cities:
    if e[0] == 'п':
        idx = new_сities.index(e)
        print(idx, e)
        new_сities.append(e)
        new_сities.pop(idx)
        #print(new_сities)

for x in range(len(new_сities)):
    print(new_сities[x])


