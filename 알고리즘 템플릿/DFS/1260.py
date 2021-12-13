import sys
sys.stdin = open('1260.txt')

n, m, v = map(int, input().split())
data = [[] for _ in range(m)]
for _ in range(m):
    s, e = map(int, input().split())
    #  단방향
    data[s].append(e)
    # 양방향 추가
    data[e].append(s)

result = [v]
visited = [False]*(n+1)
visited[v] = True

def dfs(cur, start):
    # 종료조건
    if cur == n:
        return
    
    '''
    1. node 만들기 (단방향인지 양방향)
    2. node에서 필요한 인덱스에서 for문 돌리기
    for문 안에서
    3. 방문 여부 체크
    4. 방문햇다고 표시
    5. 결과 리스트 변경
    6. 다음 재귀로 들어가기
    '''
    
    # 재귀호출부
    for i in data[start]:
        if visited[i] == False:
            visited[i] = True
            result.append(i)
            dfs(cur+1, i)

dfs(0, v)
print(result)