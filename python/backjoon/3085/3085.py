import sys, copy
sys.stdin = open('3085.txt')

N = int(input())
# print(N)
board = [input() for _ in range(N)]
# print(board)
# 가로로만
Y = [-1, 0, 1, 0]
X = [0,1 ,0 ,-1]
# def dfs(start):
maxCandy = 0
recordWidth = [[0 for _ in range(N)] for _ in range(N)]
recordHeight = [[0 for _ in range(N)] for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
# print(record)
def change(start, end):
    for i in range(N):
        for j in range(N):
            if i <= N-2 and j<=N-2:
                recordWidth = copy.deepcopy(board)
                if board[i][j] != board[i+1][j]:
                    recordWidth[i][j], recordWidth[i + 1][j] = recordWidth[i + 1][j], recordWidth[i][j]
                    checking(recordWidth)


# copy.deepcopy()
def checking(record):
    global maxCandy
    for i in range(N):
        for j in range(N):
            dfs(i,j, 0, record)

def dfs(y,x, count, record):
    if y+1 >N-1 or x+1 > N+1 or 네방향이 같으면
        return count
    else:
        for i in range(4):
            dy = y + Y[i]
            dx = x + X[i]
            if visited[dy][dx] == 1 or dy >= N or dx > N or record[dy][dx] != record[y][x]:
                pass
            else:
                visited[dy][dx] =1
                dfs(dy, dx, count+1, record)
    # return count
# 세로로만