import sys
sys.stdin = open("1476.txt")
# x = 1
# E, S, M = map(int, input().split())
# print(E,S,M)
# while x > -1:
#     if x % 15 == E and x % 28 == S and x % 19 == M:
#         break
#     if x == E or x == S or x == N:
#     x += 1
# print(x)
x = 1
E, S, M = map(int, input().split())
e, s, m = 1, 1, 1
while x > 0:
    if e > 15 :
        e -= 15
    if s > 28:
        s -= 28
    if  m > 19:
        m -= 19
    if e == E and s == S and m == M:
        print(x)
        break
    e += 1
    s += 1
    m += 1
    x += 1

# while x > 0:
#     if x % 15 == E and x % 28 == S and x % 19 == M:
#         break
#     if x % 15 == 0 and x % 28 == 0 and x % 19 == 0:
#         break
    # x-15 ,, x-28 , x-19 e,s,m나누자
    # x += 1