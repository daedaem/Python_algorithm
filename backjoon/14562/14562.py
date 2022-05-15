from collections import deque
import math
import sys

sys.stdin=open('14562.txt')

C = int(input())

def bfs(S,T, counts):
    # global S, T, temp
    if S == T:
        return counts
        # if mins > counts:
        #     mins=counts
        #     return mins
    else:
        while que:
            S, T = que.popleft()
            for i in range(3):
                S+=scoreS[i]
                T+=scoreT[i]
                counts+=1
                temp = S
                que.append([S, T])




for testcase in range(C):
    mins = math.inf
    # print(que)
    S, T = map(int, input().split())
    que = deque()
    que.append([S,T])
    temp = S
    scoreS = [1, temp, 0]
    # 내가 이기면
    scoreT = [0, 0, 3]
    counts = 0
    bfs(S,T,0)
