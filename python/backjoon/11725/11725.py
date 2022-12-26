import sys
sys.stdin = open('11725.txt')
# 파이썬 기본 재귀 깊이 제한은 1000
# 따라서, 반복 1000회 제한을 늘려줘야함.
sys.setrecursionlimit(10**6)

N = int(input())
tree = [[] for _ in range(N+1)]
parent = [False] * (N+1)
for i in range(N-1):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)
# print(tree)

def dfs(start, tree, parent):
    for i in tree[start]:
        if parent[i] == False:
            parent[i] = start
            dfs(i, tree, parent)

dfs(1, tree, parent)
for i in range(2, N+1):
    print(parent[i])
# N = int(input())
# tree = [[] for _ in range(N+1)]
# parent = [False] * (N+1)
# for i in range(N-1):
#     x, y = map(int, input().split())
#     tree[x].append(y)
#     tree[y].append(x)
# # print(tree)
#
# def dfs(start, tree, parent):
#     for i in tree[start]:
#         if parent[i] == False:
#             parent[i] = start
#             dfs(i, tree, parent)
#
# dfs(1, tree, parent)
# for i in range(2, N+1):
#     print(parent[i])

    # # visited[x] = y
    #
    # if visited[x] == False:
    #     visited[x] = y
    #     dfs(x,y)


# visited = [False] * (N+1)
# nodes = [list(map(int, input().split())) for _ in range(N-1)]
# # print(nodes)
# visited[1] = True
# infos = [0] * (N+1)
# # print(infos)
# for i in nodes:
#     if visited[i[0]] == True and visited[i[1]] == False:
#         visited[i[1]] = True
#         # 자식 자리에 부모
#         infos[i[1]] = i[0]
#     elif visited[i[1]] == True and visited[i[0]] == False:
#         visited[i[0]] = True
#         infos[i[0]] = i[1]
#     else:
#         pass
# for i in infos[2:]:
#     print(i)
#
#



#
#


