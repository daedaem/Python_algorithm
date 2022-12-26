import sys
sys.stdin = open('1959.txt')

t = int(input())
for tc in range(1, t+1):
    N, M = map(int, input().split())
    # print(N,M)
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # print(A)
    # print(B)
    if N >= M:
        result=[]
        for i in range(N-M+1):
            temp = 0
            for j in range(M):
                temp += A[j+i] * B[j]
            result.append(temp)
    else:
        result=[]
        for i in range(M-N+1):
            temp = 0
            for j in range(N):
                temp += A[j] * B[j+i]
            result.append(temp)
    print('#{}'.format(tc), max(result))


