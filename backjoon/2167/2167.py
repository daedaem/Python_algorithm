import sys
sys.stdin = open('2167.txt')
# N행 M열
N, M = map(int,(input().split()))
arranges = [list(map(int,(input().split()))) for _ in range(N)]
# print(x)
K = int(input())
for j in range(K):
    i, j, x, y = map(int, input().split())
    # print(i,j,x,y)
    sum = 0
    # i, = numlist[0]  # 1
    # j = numlist[1]  # 1
    # x = numlist[2]  # 2
    # y = numlist[3]  # 3
    for x1 in range(i-1, x):
        for y1 in range(j-1, y):
            sum += arranges[x1][y1]
    # for c in range(K):
# #     sum = 0
#     i = numlist[c][0] # 1
#     j = numlist[c][1] #1
#     x = numlist[c][2] #2
#     y = numlist[c][3] #3
#
# #     for x1 in range(i-1,x):
#         for y1 in range(j-1, y):
#             sum += arranges[x1][y1]
#     print(sum)


#     arranges[i][j]
# # x =
# # y =
# print(numlist)