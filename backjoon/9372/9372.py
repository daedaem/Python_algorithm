import sys
sys.stdin = open('9372.txt')

def dfs(n, cnt):
    visited[n] = True
    for i in tree[n]:
        if visited[i] == False:
            cnt = dfs(i, cnt+1)
    return cnt

T = int(input())
for index in range(1, T+1):
    N, M = map(int, input().split())
    visited = [False] * (N+1)
    tree = [[] for _ in range(N+1)]
    cnt = 0
    result = 0
    for i in range(M):
        a, b = map(int, input().split())
        # print(a,b)
        tree[a].append(b)
        tree[b].append(a)

    # print(tree)
    # dfs(1)
    # for i in tree[n]:
# print(dfs(1, cnt))
    cnt = dfs(1, 0)
    print(cnt)
# print(cnt)


import sys














