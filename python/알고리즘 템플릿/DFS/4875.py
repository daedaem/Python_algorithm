import sys
sys.stdin = open('4875.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    visited = [[False]*N for _ in range(N)]
    x, y = 0, 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 3:
                x, y = i, j
    visited[x][y] = True
    result = 0

    def dfs(x, y):
        global result

        # 종료 조건
        if arr[x][y] == 2:
            result = 1
            return

        # 재귀호출부
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            # 1. 이동이 가능한 범위
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == False:
                if arr[nx][ny] == 0 or arr[nx][ny] == 2:
                    visited[nx][ny] = True
                    dfs(nx, ny)

    dfs(x, y)
    print(result)