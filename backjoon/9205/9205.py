import sys
from collections import deque
sys.stdin=open('9205.txt')

queue = deque()
def bfs(start, end):
    deque.pop()
maxdis = 10000
t = int(input())

def bfs(cnt):
    # que.append()
    while que:
        y, x = que.pop()
        for i in range(4):
            dy = Y[i]+y
            dx = X[i]+x
            if dy >= M or dy<0 or dx >=N or dx <0 or record[dy][dx] == 1:
                pass
            # elif
            else:
                que.append([dy,dx])
                record[dy][dx] = 1
                cnt+=1
    if cnt != 0:
        return result.append(cnt)
    else:
        pass

for tc in range(1, t):
    Y = [-1, 0, 1, 0]
    X = [0, 1, 0, -1]
    n=int(input())
    # home==start
    start = list(map(int, input().split()))
    conv = [list(map(int, input().split())) for _ in range(n)]
    # end =rockFestival
    end = list(map(int, input().split()))
    # print(end[1])
    record = [[0] * (end[0]) for _ in range(end[1])]
    for i in range(end[0]):
        for j in range(end[1]):
            # record[i][j]
            # pass
    print(record)





