import sys
sys.stdin = open('1012.txt')
sys.setrecursionlimit(99999)
# 방문표시 만들기
# 시작점을 찾는다.
# 시작점으로부터 1이면 방문표시하고 0으로 바꾼다
# ? 방문표시에다가 0으로 바꾸는건지
# ? 입력값을 맵을 만든 원본에 0으로 바꾸는건지
def DFS(y, x):
    # for i in range(N):
    #     for j in range(M):

    for i in range(4):
        dy = y + Y[i]
        dx = x + X[i]
        # print(baechu_map)
        if dx < 0 or dy < 0 or dx > M or dy > N or baechu_map[dy][dx] == 0:
            pass
        else:
            baechu_map[dy][dx] = 0
            DFS(dy, dx)

T= int(input())
for index in range(T):
    M,N,K = map(int, input().split())
    # 배추 위치 받기
    baechu = [list(map(int, input().split())) for _ in range(K)]
    # 배추위치를 표시해줄 baechu_map 만들기
    # baechu_map = [[0 for _ in range(M)] for _ in range(N)] - > 인덱스 오류나서 생각해보니 0부터 시작하니 M, N 인덱스 사용하면 지도에 표시불가
    baechu_map = [[0 for _ in range(M+1)] for _ in range(N+1)]
    # 배추위치를 1값으로 표시해주기
    for i in range(len(baechu)):
        x = baechu[i][0]
        y = baechu[i][1]
        baechu_map[y][x] = 1
    # print(baechu_map)

    #상하좌우
    Y=[-1, 1, 0, 0]
    X=[0, 0, -1, 1]
    jirungee = 0

    for i in range(N):
        for j in range(M):
            if baechu_map[i][j] == 1:
                jirungee += 1
                DFS(i, j)
    print(jirungee)