n = int(input())
count = 0
for x in range(n+1):
    div = []
    for i in range(x - 1, 1, -1):
        if (x % i) == 0:
            div.append(i)
            count = len(div)
    if count >=6 and len(div)!=0 :
        print(x, div)