import sys
sys.stdin = open("15469.txt")
N, M = map(int, input().split())
# print(N, M)
# 수열만들 숫자 numbers
numbers = list(range(1, N+1))
# print(numbers)
visited = [0] *(N+1)
# print(visited)
temp = []
result = []
def backtracking(temp):
    # 만든 수열 길이가 주어진 조건과 일치하면 결과에 추가
    if len(temp) == M:
        result.append(temp)
    # 아직 수열이 덜 완성됬다면
    else:
        for i in numbers:
            # 방문했거나 이미 만든수열이라면 패스
            if visited[i] == 1 or i in temp:
                pass
            else:
                # 방문처리
                visited[i] == 1
                # 만들고 있는 수열에 추가
                backtracking(temp+[i])
    return result
backtracking(temp)

for i in result:
    print(*i)


