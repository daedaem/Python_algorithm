#  n자리 m진수
# 3자리 5진수
# 000 001 002 003 004
# ... 444
'''
# 1 번 탬플릿
# 완전탐색
n = 3
m = 5
data = [0]*n

def dfs(cur):
    #  종료 조건
    if cur == 3:
        print(data)
        return

    # 재귀호출부 -> 어떤 방법으로 재귀를 들어갈것이냐
    for i in range(m):
        data[cur] = i
        dfs(cur+1)

dfs(0)
'''
'''
# 2번 템플릿
n= 3
m = 5
data = [0]*n
# 순열 = 중복은 없어야해 근데 순서는 상관이 있는것
visited = [False]*m

def recur(cur):
    if cur == 3:
        print(data)
        return

    for i in range(m):
        if visited[i] == False:
            visited[i] = True
            data[cur] = i
            recur(cur+1)
            visited[i] = False

recur(0)

'''

# 3번 템플릿 -> 조합
# 순서도 상관이 없고 중복도 안됨!!
n = 3
m = 5
data = [0] * n

def recur(cur, start):
    if cur == n:
        print(data)
        return

    for i in range(start, m):
        data[cur] = i
        recur(cur+1, i+1)

recur(0, 0)


