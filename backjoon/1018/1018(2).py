import sys
sys.stdin=open('1018.txt')
# 1.전부 0으로 2차원 배열 만들고
# w부터 시작하는걸로 체크
# b부터 시작하는걸로 체크
# 갯수 젤 작은거 걍 구하자
# 1번은 포기

# 2.
# 2-1 제대로 된 체스판 2가지 만든다.
# 2-2 a. 홀이b면 짝이W b.홀이W면 짝이B일때 두가지로 비교
N, M = map(int, input().split())
# print(N, M)
board = [list(input()) for _ in range(N)]
# b검은색은 0 w흰색은 1로
# 체스판 제대로 된거 2가지 버젼 만들기
chess_v1 = [['B']*M for _ in range(N)]
chess_v2 = [['W']*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if i % 2:
            if j % 2:
                chess_v1[i][j]='B'
                chess_v2[i][j] = 'W'
            else:
                chess_v1[i][j] = 'W'
                chess_v2[i][j] = 'B'
        else:
            if j % 2:
                chess_v1[i][j]='W'
                chess_v2[i][j] = 'B'
            else:
                chess_v1[i][j] = 'B'
                chess_v2[i][j] = 'W'
# 체스판 두가지 버젼 만들고 제시한 보드를 모두 탐색하면서 비교
# 틀리면 횟수 +1
result = []
temp_v1 = 0
tem_v2 = 0
cnt_ver1=0
cnt_ver2=0
# print(len(board))
for i in range(N-7): # 2
    for j in range(M-7): # 5
        cnt_ver1, cnt_ver2 = 0, 0
        for x in range(8):
            for y in range(8):
                if board[x+i][y+j] != chess_v1[x+i][y+j]:
                    cnt_ver1 +=1
                if board[x+i][y+j] != chess_v2[x+i][y+j]:
                    cnt_ver2 +=1
        result.append(cnt_ver1)
        result.append(cnt_ver2)
print(min(result))

        #             if x < 7 and y < 7 and board[x+i][y+j+1] !='W':
        #                 board[x + i][y + j + 1]= 'W'
        #                 cnt +=1
        #             if x < 7 and y < 7 and board[x+i+1][y+j] != 'W':
        #                 board[x + i + 1][y + j]= 'W'
        #                 cnt +=1
        #         if board[x+i][y+j] =='W':
        #             if x < 7 and y < 7 and board[x+i][y+j+1] !='B':
        #                 board[x + i][y + j + 1] = 'B'
        #                 cnt += 1
        #             if x < 7 and y < 7 and board[x+i+1][y+j] != 'B':
        #                 board[x + i + 1][y + j] = 'B'
        #                 cnt += 1
        # result.append(cnt)
# print(result)
# print(chess)
# for i in range(N-7): # 2
#     for j in range(M-7): # 5
#         for x in range(8):
#             for y in range(8):
#                 if chess[x+i][y+j] == 1:
#                     chess[x+i][y+j] = 0
#                 if board[x+i][y+j] == 0
#                     chess[x+i][y+j] = 1

                # if y == 0:
                #     if x!= 7 and y!=7 and board[x+i][y+j] == 'B':
                #         if board[x+i][y+j+1] != 'W' or board[x+i+1][y+j] != 'W':
                #             cnt += 1
                #
                #
                #     elif x!= 7 and y!=7 and board[x+i][y+j] == 'W':
                #         board[x + i][y + j + 1] == 'B'
                #         board[x + i + 1][y + j] == 'B'

                # board[x+i][y+j]

