import sys
sys.stdin = open('5189.txt')

def dfs(cur, num, answer):
    if cur == N-1:
        result.append(answer)
        return
    else:
        for i in num:
            if visit[i] == True:
                continue
            else:
                if visit[i] == False:
                    visit[i] = True
                    answer.append(i)
                    dfs(cur+1, num, answer)
                    visit[i] = False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    box = [list(map(int, input().split())) for _ in range(N)]
    # print(box)
    num = list(range(2, N+1))
    # print(num)
    visit = [False] * (N+1)
    result = []
    answer = [1]
    dfs(0, num, answer)
    print(answer)