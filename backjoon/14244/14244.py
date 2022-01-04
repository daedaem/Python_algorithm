import sys
sys.stdin = open('14244.txt')

n, m = map(int, input().split())

tree = [[] for _ in range(n+1)]
number_list = list(range(n))
# 맨 앞 0이 무조건 리프1를 차지하니까
# 리프 수 m이 2이면 그냥 순서대로 출력
if m == 2:
    for i in range(n-1):
        print(i, i+1)
# 만약 리프수가 2이상이면
# n-m까지 순서대로 출력하고 나머지는 n-m과 다 연결됨
# ex) 7, 3 이면  0-1-2-3-4 4-5 4-6
else:
    for i in range(n-m):
        print(i, i+1)
    for i in range(n-m+1, n):
        print(n-m, i)
