a = float(input())
b = float(input())
c = float(input())
d = (b**2)+(-4*a*c)
if d>0:
    x1 = (-b-d**0.5) / (2*a)
    x2 = (-b + d ** 0.5) / (2 * a)
    print('x1 =', x1,', x2 =', x2)
if d==0:
    x = (-b)/(2*a)
    print('x =', x)
if d<0:
    print('нет корней')

