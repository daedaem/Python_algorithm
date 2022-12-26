import sys
sys.stdin=open('10157.txt')
#c가로, r세로
C, R = map(int, input().split())
K = int(input())
record = [[0] * (C) for _ in range(R)]
# print(record)
#벽을 -1로 설정
# for z in range(0, -2, -1):
#     for i in range(C+2):
#         record[z][i] = -1
#         for j in range(R+2):
#             record[j][z] = -1
# print(record)
# [K -1 -1- 1 -> 0] [0]
x = [0, 1, 0, -1]  # 상 우 하 좌
y = [-1, 0, 1, 0]
#
w=0
h=R-1
X=0
Y=0
cnt=1
while cnt < C*R+1:# 계속반복
    for i in range(4):# 상우하좌
        # print(cnt)
        # print(i)
        while h >= 0 and h <= R-1 and w >= 0 and w <= C-1:
                # print(w)
            # print(h, w)
            h += y[i]
            w += x[i]
            cnt += 1
            record[h][w] = cnt
        if h + y[i] >= R or h + y[i] < 0:
            h -= y[i]
        if w + x[i] >= C or w + x[i] < 0:
            w -= x[i]
        # print(w)
        #  c-1 r-1 되는 부분 처리해야함
print(record)

#

#             else:
#                 record[h + y[i]][w + x[i]] = cnt
#                 cnt += 1
# #

# print(cnt)
# print(record)

    # for i in d:
    #     while x+i
    # record[x+i][y+j] = cnt
    # cnt += 1
#
# # #     while
# import sys
# sys.stdin=open('10157.txt')
# #c가로, r세로
# C, R = map(int, input().split())
# K = int(input())
# record = [[0] * C for _ in range(R)]
# # print(record)
# #벽을 -1로 설정
# # for z in range(0, -2, -1):
# #     for i in range(C+2):
# #         record[z][i] = -1
# #         for j in range(R+2):
# #             record[j][z] = -1
# # print(record)
# # [K -1 -1- 1 -> 0] [0]
# x = [0, 1, 0, -1] # 상 우 하 좌
# y = [-1, 0, 1, 0]
# #
# w=0
# h=R-1
# cnt = 1
# point=0
# while cnt < C*R+1:
#     for i in range(4):
#         # print(i)
#         while record:
#             if h+y[i] < 0 or h+y[i] >= R or w+x[i] < 0 or w+x[i] >= C or record[h+y[i]][w+x[i]] != 0:
#                 break
#             else:
#                 record[h + y[i]][w + x[i]] = cnt
#                 cnt += 1
#
# # print(cnt)
# print(record)
#
#     # for i in d:
#     #     while x+i
#     # record[x+i][y+j] = cnt
#     # cnt += 1
# #
# # #     while