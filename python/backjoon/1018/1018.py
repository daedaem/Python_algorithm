import sys
sys.stdin = open("1018.txt")
N, M = map(int, input().split())
# print(N, M)
chess = [input() for _ in range(N)]
print(chess)
sum = []
# 9행 10열
# 체스에서 8x 8 칸씩 순회하는거
for i in range(M-8+1): #   0 1
    for j in range(N-8+1): # 0 12
        for x in range(8): # 0 1 2 # 0 12
            for y in range(8):
            #맨처음이 w라고 가정, 처음을 안바꾸는게 최선책
                chess[j][i+c]
            if chess[i][j] == 'W':
                chess[i][j+1]


            if chess[i+z][j+z] == 'W':
                if chess[i+z+1][j+z] !='B':
                    chess[i + z + 1][j+z] = 'B'
                    cnt += 1
                if chess[i+z][j+z+1] !='B':
                    chess[i + z][j+z+1] = 'B'
                    cnt += 1
        # 맨처음이 w라고 가정, 맨 처음을 바꾸고 그담것들도 아니면 바꾸기
            if chess[i+z][j+z] == 'w':
                if chess[]:

            if chess[i+z][j+z] == 'b'
                if chess[i+z+1][j+z] !='z'
                    chess[i + z + 1][j+z] = 'z'
                    cnt += 1
                if chess[i+z][j+z+1] !='z'
                    chess[i + z][j+z+1] = 'z'
                    cnt += 1

            # 맨처음이 b라고 가정
