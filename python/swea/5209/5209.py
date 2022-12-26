import sys
sys.stdin=open('5209.txt')

def dfs(cur, N):
    global ans
    global total
    if cur == N:
        if ans > total:
            ans = total
        return
    else:
        for i in range(N):
            if visit[i] == True:
                continue
            else:
                visit[i] = True
                total += factory[cur][i]
                dfs(cur+1, N)
                visit[i] = False
                total -= factory[cur][i]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    factory = [list(map(int, input().split())) for _ in range(N)]
    print(factory)
    visit = [False]*(N+1)
    ans = 100*15
    total = 0
    dfs(0, N)
    print(ans)

