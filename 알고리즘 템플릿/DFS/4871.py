import sys
sys.stdin = open('4871.txt')

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    node = [[] for _ in range(V+1)]

    for _ in range(E):
        u, v = map(int, input().split())
        node[u].append(v)
    s, e = map(int, input().split())
    visited = [False] * (V+1)
    visited[s] = True
    result = 0

    def dfs(start):
        global result

        if start == e:
            result = 1
            return

        for i in node[start]:
            if visited[i] == False:
                visited[i] = True
                dfs(i)

    dfs(s)
    print(result)