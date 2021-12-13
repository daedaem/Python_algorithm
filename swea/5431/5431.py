import sys
sys.stdin = open('5431.txt')
# 테스트 케이스

T = int(input())

# 수강생 1~N, 과제 제출 자 수 K
# 과제제출 x 오름차순
# N만큼 range나열하고 낸 학생만 빼고
# 나머지들 오름차순 정렬
for index in range(1, T+1):
    N, K = map(int, input().split())
    kinfo = list(map(int, input().split()))
    totalmember = list(range(1, N+1))
    # print(kinfo)
    # print(totalmember)
    # kinfo에서 하나씩 꺼내서 totalmember의 인덱스로 사용하여 (-1) 0으로 바꿔준다. or delete
    lazypeople = []
    for i in kinfo:
        for j in range(len(totalmember)):
            if totalmember[j] == i:
                totalmember[j] = 0
    # print(totalmember)
    x = sorted(totalmember)
    result = []
    for i in x:
        if i !=0:
            result.append(i)
    print('#{}'.format(index), *result)

