import sys
sys.stdin=open('4466.txt')

t = int(input())
for tc in range(1, t+1):
    N,K = map(int, input().split())
    # print(N,K)
    scores = list(map(int,input().split()))
    # print(scores)
    scores.sort(reverse=True)
    # print(scores)
    result = 0
    for i in range(K):
        result += scores[i]
    print('#{}'.format(tc), result)
#5개 중 3개