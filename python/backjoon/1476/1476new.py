import sys
sys.stdin=open('1476.txt')

E, S, M = map(int, input().split())
print(E,S,M)
e = 0
s= 0
m = 0
cnt = 1
# cnt 15 0이되면 그걸 0
while cnt:
    e= cnt%15
    s= cnt%28
    m= cnt%19
    if cnt % 15 == 0:
        e = 15
    if cnt % 28 == 0:
        s = 28
    if cnt % 19 == 0:
        m = 19
    if e == E and s == S and m == M:
        break
    cnt += 1
print(cnt)
