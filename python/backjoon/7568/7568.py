import sys
sys.stdin = open('7568.txt')
N = int(input())
# print(N)
x = [list(map(int, input().split())) for _ in range(N)]
# 스택 이용해서 순서별로 추가하자
# 각 리스트의 인덱스 둘다 비교해서 둘다 크면 sum + 1
# 리스트에 0 3개 든걸로 리스트 만들어서 기록하자
record = [1 for _ in range(N)]
print(record)
# print(record) 인덱스 0 자기가 더 큰거 1은 비김 2는 짐
for i in range(N): # 0 1 2 3 4
    if i == 4:
        break
    for c in range(1, N-i): #
        if x[i][0] > x[i+c][0] and x[i][1] > x[i+c][1]:
            record[i+c] += 1
        if x[i][0] > x[i+c][0] and x[i][1] < x[i+c][1]:
            pass
        if x[i][0] < x[i+c][0] and x[i][1] > x[i+c][1]:
            pass
        if x[i][0] < x[i+c][0] and x[i][1] < x[i+c][1]:
            record[i] += 1
print(*record)