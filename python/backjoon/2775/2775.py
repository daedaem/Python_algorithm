import sys
sys.stdin = open("2775.txt")

T= int(input())
for tc in range(T):
    K = int(input())
    N = int(input())
    # dp = [[i for i in range(N+1)] for _ in range(K+1)]
    dp = [i for i in range(N+1)]
    # print(dp)
    # for i in range(1, N+1):
    #     dp [i] += dp[i-1]
    for i in range(K):
        for j in range(1, N+1):
            dp[j] += dp[j-1]
    print(dp[-1])
    # print(dp)
    # for f in range(, )
