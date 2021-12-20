import sys
sys.stdin = open('2468.txt')
sys.setrecursionlimit(99999)

def dfs(y, x, cnt, z):
    visited[y][x] == 1

    for i in range(4):
        dy = y + Y[i]
        dx = x + X[i]

        if dx < 0 or dy < 0 or dx > N-1 or dy > N-1 or visited[dy][dx] == 0:
            pass
        else:
            if visited[dy][dx] == 0:
                pass
            else:
                visited[dy][dx] = 0
                dfs(dy, dx, cnt, z)
    return cnt

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# print(arr)
visited = [[0] * N for _ in range(N)]
# print(visit)
Y=[-1,1,0,0]
X=[0,0,-1,1]
max_height = 0
# 가장 높은 높이 찾기 = max_height
for i in range(N):
    if max_height < max(arr[i]):
        max_height = max(arr[i])
# print(max_height)
#
# for x in range(max_height+1):
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] <= x:
#                 dfs(i, j, cnt)
# 특정 숫자 크면 방문처리하고 이동
cnt = 0
result = []
#0부터 가장 높은 높이까지 z로 기준 맞춰놓고
# 계속해서 방문 그래프 만들기

for z in range(max_height+1):
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] <= z:
                visited[i][j] = 0
            else:
                visited[i][j] = 1
    # 높이에 맞게끔 새롭게 visited에 0과 1로 갈수 있는 길을 나타내는 그래프 만든 다음 dfs 돌리기
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 1:
                cnt+=1
                dfs(i, j, cnt, z)
    # result에는 높이기준별로 나오는 영역 수 담음
    result.append(cnt)
print(max(result))

