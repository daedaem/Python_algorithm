import sys
sys.stdin=open('10162.txt')

T = int(input())
a= 300
b=60
c=10

if T % 10 !=0:
    print(-1)
else:
    if T < a:
        pass
    elif T < b:
        pass
        print(0,b,c)
    else:
        print(0, 0, T//c)

def dfs(start, end):
    if end >= T:
        return start
    else:
