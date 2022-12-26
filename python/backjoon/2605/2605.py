import sys
sys.stdin = open('2605.txt')
# 뽑을 수 있는 숫자는 N
# 학생수 t
t = int(input())
# 학생들이 뽑은 숫자들 리스트
ide = list(map(int, input().split()))

# 순서를 담을 result 변수
result = []
# n은 학생번째 수, ide[n-1]은 학생이 뽑은 숫자
# 헷갈리니까 ide[n-1]을 choicen변수에 담자
# n 번째 학생은 현재까지 생성된 리스트의 길이 - 뽑은 숫자에 추가해야함
for n in range(1, t+1):
    choicen = ide[n - 1]
    result.insert(len(result)-choicen, n)
print(*result)

# t번째 학생이 뽑을 수 있는 번호 리스트
# for n in range(1, t+1):
#     nlist = list(range(n))

