import operator
n = int(input())

num = []
for x in range(n+1):
    count = 0
    div = []
    for i in range(x - 1, 1, -1):
        if (x % i) == 0:
            div.append(i)
            count = len(div)
    #print(x, div)
    num.append((count,x))

#print(num)
num.sort(key=operator.itemgetter(1), reverse=True)
num.sort(key=operator.itemgetter(0), reverse=True)
#print(num)

for i in num:
    print(i[1], end=' ')