import sys
# from collections import deque
sys.stdin= open('2579.txt')

N = int(input())
stairs = [0]
# print(visited)
max_value = 0

for _ in range(N):
    x = int(input())
    stairs.append(x)

if dp[i-1] < dp[i-2]:
    dp[i] = dp[i-1] + stairs[i]
else:
    dp[i] = dp[i-2] + stairs[i]




# record = []
# print(x)
print(stairs)
# for i in range(1,3):
    # bfs(i, 6, val)


# que = deque()
# values = []
# val = []
#
# def bfs(x):
#     while que:
#         value = que.popleft()
#         value.append(x)
#
#         que.append()

# def bfs(start, end, val):
#     if start >= end:
#         global values
#         values.append(val)
#         val = []
#         return
#     else:
#         if len(val) >= 2 and val[-1] == start - 1 and val[-2] == start-2:
#             pass
#         else:
#             val.append(start)
#             que.append(val)
#         # visited[start] = 1
#             while que:
#                 que.popleft()
#                 for i in range(1, 3):
#                     bfs(start+i, N, val)
#             #         visited[start] = 0
#             #         result.pop()



# que = []

#
#
#
# # def sumstair(x, visited):
# #     if while
#
# # 10 30 35 55 65 75
# #
# # 1
# # 1       10    10
# #
# # 2
# # 12      30          50
# # 2       20
# 1
#
# # 3
# # 1,3     25
# # 2,3     35          60
# #
# 1
# 2
# # 4
# # 1,2,4   55
# # 1,3,4   50          150
# # 2,4     45
# #
# 12
# 13
# 2
#
# # 5
# # 1   2   4   5       65      200
# # 1,  3   5           35
# # 2   3   5           45
# # 2   4   5           55
# #
# 124
# 13
# 23
# 24
#
# # 6
# # 1   2   4   6       75
# # 1   3   4   6       70
# # 1   3   5   6       55
# # 2   3   5   6       65
# # 2   4   6           65 ?
# 124
# 134
# 135
# 235
# 24
#
# # 7
# # 1   2   4   5   7
# # 1   2   4   6   7
# # 1   3   4   6   7
# # 1   3   5   7
# # 2   3   5   7
# # 2   4   5   7
# # 2   4   6   7
# 1245
# 1246
# 1346
# 135
# 235
# 245
# 246
# # 8
# # 1   2   4   5   7   8
# # 1   2   4   6   8
# # 1   3   4   6   8
# # 1   3   5   6   8
# # 1   3   5   7   8
# # 2   3   5   6   8
# # 2   3   5   7   8
# # 2   4   5   7   8
# # 2   4   6   8
