import sys

sys.stdin = open('10158.txt')
# 격자 가로 w, 세로 h
w, h = map(int, input().split())
# print(w, h)
# 현재위치 가로 p, 세로 q, 세로 인덱스는 2차원 배열에서 반대 즉, 세로칸에서 현재위치 빼기
p, q = map(int, input().split())
t = int(input())
# p-1 q+1
# q = h - q
# print(q)
x = 1
y = 1
# 맨 처음 w에서 p빼고를 p로나누고 h를 q로 나눠서
t= t%(w*h)
while t > 0: # 5, 0
    if p + x > w:
        x = -1
    elif p + x < 0:
        x = 1
    if q + y > h:
        y = -1
    elif q + y < 0:
        y = 1
    p += x
    q += y
    t -= 1

print(p, q)

# 1위치 6
# 2 3 4 5 6 5 4 3 2 1 0 1 2 3 4 5 6 5 4 3 2 1 0
#  10 12 22  24
# +12 +2
# 0 1
# 6 1
#
# (6-1) *2 (1-0) *2
#
# 4 0
# 8 16
# 8 8
#
# 4 1
# 6 8 14 16 22 24
# 6 2 6 2 6 2
#
# 4 2
# 4 8
# 4 8 4 8
#
# 4 3
# 2 8 10 16
#
# (h-q) *2, (q+0) *2
#
# 4 4
