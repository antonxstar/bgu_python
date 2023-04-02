# x = 70
# stroka =''
#
# while True:
#     stroka += str(x%3)
#     x=x//3
#     if x<3:
#         stroka += str(x)
#         break
#
# print(stroka)
# print(stroka[::-1])

x = 73
stroka =''

while True:
    if (x%3) == 2:
        stroka += 'i'
        x = x // 3 + 1
    else:
        stroka += str(x % 3)
        x=x//3

    if x<3:
        stroka += str(x)
        break

print(stroka)
print(stroka[::-1])


# def conver_to3a(x):
#     stroka = ''
#     while True:
#         stroka += str(x % 3)
#         x = x // 3
#         if x < 3:
#             stroka += str(x)
#             break
#     return stroka[::-1]
#
# print(conver_to3(73))