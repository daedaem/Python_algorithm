import sys
sys.stdin=open('10157.txt')

T = int(input())
for tc in range(1, T+1):
    C, R = map(int, input().split())
    # print(C, R)
    K = int(input())
    # print(K)
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    record = [[0] * C for _ in range(R)]
    # print(record)
    # 방향벡터 인덱스
    d = 0
    #현재
    x = 0
    y = R - 1
    # 좌석번호
    cnt = 1
    # 관객 대기번호가 좌석 총 수보다 크면 0출력
    if C*R < K:
        print(0)
    # 대기번호가 좌석수안이라 배정할 수 있다면
    else:
        while cnt <= C*R:
            record[y][x] = cnt
            x = x + dx[d]
            y = y + dy[d]
            cnt += 1
            if 0 > x + dx[d] or x + dx[d] > C - 1 or 0 > y + dy[d] or y + dy[d] > R - 1 or record[y+dy[d]][x+dx[d]] != 0:
                d += 1
                if d > 3:
                    d = d % 4

        for i in range(R):
            for j in range(C):
                if record[i][j] == K:
                    print(j+1, R-i)



















    # import sys
    # sys.stdin=open('10157.txt')
    # # 공연장 가로 길이 C,  세로 길이 R
    # C, R = map(int, input().split())
    # # print(C,R)
    # # 관객좌석번호
    # K = int(input())
    # # 공연장 좌석 입력하기 위한 records
    # records = [[0] * C for _ in range(R)]
    # #상 우 하 좌 로 움직이도록 하는 x, y 좌표
    # # x좌표
    # x=[0, 1, 0, -1]
    # # y좌표
    # y=[-1, 0, 1, 0]
    # #하 우 상 좌
    # # x좌표
    # # x=[0, 1, 0, -1]
# # # y좌표
# # y=[1, 0, -1, 0]
# # cnt = 1
# # while records:
# #     if cnt > C*R:
# #         break
# #     else:
# #         for i in range(4):
# #             for h in range(R): #0, 1, 2~ 5
# #                 for w in range(C):# 0~6
# #                     if records[h+y[i]][w+x[i]] != 0 or h+y[i]<0 or h+y[i]>R or w+x[i] <0 or h+y[i]>C:
# #                         break
# #                         # 6
# #                     else:
# #                         records[h+y[i]][w+x[i]] += cnt
# #                         cnt +=1
# # print(records)
#
# # 관객 좌석 번호 입력을 위한 변수 cnt
# cnt = 1
# # 관객 좌석 가로 w, 세로 h+
# w = 0
# h = R-1 #5
# while cnt < C*R:
#     for i in range(4):
#         print(i) # 0 0
#         # if h < 0:
#         #     h -= y[i-1]
#         # elif h > R:
#         #     h -= y[i-1]
#         # if w < 0:
#         #     w -= x[i-1]
#         # elif w > C:
#         #     w -= x[i-1]
#         while records[h+y[i]][w+x[i]] == 0 and h+y[i] >=0 and h+y[i] <R and w+x[i] >=0 and w+x[i] <C:
#             records[h + y[i]][w + x[i]] = cnt
#             h = h+y[i]
#             w = w+x[i]
#             cnt += 1
# print(records)
#
#
#
