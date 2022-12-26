import sys
sys.stdin = open('5431.txt')
# 테스트 케이스

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    # print(N, K)
    all_people = list(range(1, N+1))
    # print(all_people)
    students_list = list(map(int, input().split()))
    # print(students_list)
    result = list(set(all_people) - set(students_list))
    result.sort
    print('#{}'.format(tc), *result)
