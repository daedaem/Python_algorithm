import sys
sys.stdin = open('5102.txt')
#
# T = int(input())
# for tc in range(1, T+1):
#     V, E = map(int, input().split())
#     node = [[] for _ in range(V+1)]
#     for _ in range(E):
#         x, y = map(int, input().split())
#         node[x].append(y)
#         node[y].append(x)
#     s, e = map(int, input().split())
#     visited = [0]*(V+1)
#     queue = []
#
#     # def bfs(s):
#     #     queue.append(s)
#     #     visited[s] = 0
#     #
#     #     while queue:
#     #         lo = queue.pop(0)
#     #
#     #         for i in node[lo]:
#     #             if visited[i] == 0:
#     #                 visited[i] = visited[lo] + 1
#     #                 queue.append(i)
#
#     def bfs(s):
#         depth = 0
#         queue.append([s, depth])
#         visited[s] = 0
#
#         while queue:
#             lo, depth = queue.pop(0)
#
#             if lo == e:
#                 print(depth)
#                 break
#
#             for i in node[lo]:
#                 if visited[i] == 0:
#                     visited[i] = 1
#                     queue.append([i, depth+1])
#
#     bfs(s)
#     # print(visited[e])
#
#


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[] for _ in range(V+1)]
    for i in range(E):
        S, G = map(int, input().split())
        arr[S].append(G)
        arr[G].append(S)
        # map(int)
    S, G = map(int, input().split())
    visit=[False] * (V+1)
    result = [S,]
    visit[S] = True
    answer = V-1
    # print(visit)
    # print(arr)
    def dfs(cur, cnt, result):
        global answer
        result.append(cur)
        # print(result)
        if cur == G:
             if answer > cnt:
                 answer = cnt
             return
        else:
            for u in arr[cur]:
                if visit[u] == False:
                    visit[u] = True
                    dfs(u, cnt+1, result)
                    visit[u] = False
        result.pop()
    dfs(S, 0, result)
    # print('#{}'.format(tc), answer)
