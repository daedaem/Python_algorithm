import sys
sys.stdin=open('1769.txt')
#
# def checker(x):
#     cnt = 0
#     num = [0,0]
#     while len(str(x)) > 1:
#         x = str(num)
#         for i in range(len(list(x))):
#             # print(x)
#             num += int(list(x[i])
#         num = list(str(num))
#         print(num)
#         cnt += 1
#
#         if int(x)% 3 == 0:
#             print(cnt)
#             print('YES')
#         else:
#             print('NO')

x = input()
x_str = str(x)

cnt = 0
while len(x_str) > 1:
    newx = 0
    for i in x_str:
        newx += int(i)
        # print(i)
        # print(newx)
    x_str = str(newx)
    cnt += 1

if int(x_str) % 3:
    print(cnt)
    print('NO')
else:
    print(cnt)
    print('YES')


# x_str = str(x)
# num = 0
# cnt = 0
# checker(x)
# while len(x_str) > 1:
#     x = num
#     num = int(num)
#     for i in range(len(x_str)):
#         # print(x)
#         num += int(x_str[i])
#     num = str(num)
#     cnt += 1
#     if int(x_str)% 3 == 0:
#         print(cnt)
#         print('YES')
#         break
#     else:
#         print(cnt)
#         print('NO')
#         break
