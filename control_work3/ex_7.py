coords = [(1,5), (2,3), (6,1)]
print(coords)

print(sorted(coords, key=lambda x: x[0]+x[1]))
print(sorted(coords, key=sum))


# double = lambda x: x*2
# print(double(5))
# print(type(double))
# print(type(lambda x: x*2))
#
# def func(x):
#     return x*2
#
# func2 = func
#
# print(func2(5))