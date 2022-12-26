import sys
sys.stdin=open('12851.txt')
from collections import deque


def bfs(x, y, cnt):
    global result
    global mins
    queue = deque()
    queue.append((x, y, cnt))
    visited.append(x)
    while deque:
        x , y, cnt = queue.popleft()
        # print(x,y)
        for i in range(3):
            if i <= 1:
                dx = x + X[i]
            else:
                dx = x * X[i]
            if dx == K:
                if cnt <= mins:
                    mins = cnt
                    result.append(mins)
                elif cnt > mins:
                    return result
                #     result.append(mins)
                else:
                    pass
            elif dx < 0:
                pass
            elif dx > 100000:
                pass
            elif dx == N:
                pass
            elif (dx, y, cnt) in queue:
                pass
            elif dx in visited:
                pass
            else:
                queue.append((dx, y, cnt+1))


N, K = map(int, input().split())
# print(N)

X = [-1, 1, 2]
mins = 999999999
cnt = 1
visited = []
result = []
if N == K:
    print(0)
else:
    print(bfs(N, K, cnt)[0])
print(len(result))