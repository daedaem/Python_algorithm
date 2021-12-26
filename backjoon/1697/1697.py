import sys
from collections import deque
sys.stdin = open('1697.txt')

def bfs(x, y, cnt):
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
                # 만약 도착지에 왔다면
            if dx == K:
                return cnt

            # 음의 정수로 가면 쓸데 없는 움직임
            elif dx < 0:
                pass
            # 도착지점이 동생 2배보다 클 필요 없다
            elif dx > K*2:
                pass
            # 중복된 수를 넣을 필요 없음
            # elif dx == N:
            #     pass
            elif (dx, y, cnt) in queue:
                continue
            else:
                queue.append((dx, y, cnt+1))

N, K = map(int, input().split())
# print(N)

X = [-1, 1, 2]
cnt = 1
visited = []
if N == K:
    print(0)
else:
    print(bfs(N, K, cnt))
