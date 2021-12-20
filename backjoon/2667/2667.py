import sys
sys.stdin = open('2667.txt')

# 최단거리도 아니고 쭉 가도 되니까 dfs

def dfs(y, x, cnt):
    for i in range(4):
        dy = y + Y[i]
        dx = x + X[i]
        if dy < 0 or dx < 0 or dy > N-1 or dx > N-1 or towns[dy][dx] == 0:
            pass
        else:
            if visited[dy][dx] == 1:
                pass
            else:
                visited[dy][dx] = 1
                dfs(dy, dx, cnt)
    cnt += 1

N = int(input())
towns = [list(map(int, input())) for _ in range(N)]
# print(towns)
Y = [-1, 1, 0, 0]
X = [0, 0, -1, 1]
visited = [[0] * N for _ in range(N)]
# print(visited)
cnt = 0
for i in range(N):
    for j in range(N):
        if towns[i][j] == 1:
            dfs(i, j, cnt)
print(towns)
print(visited).

