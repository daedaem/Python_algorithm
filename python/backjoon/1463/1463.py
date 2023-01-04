import sys
sys.stdin = open("1463.txt")

X = int(input())
dp = [0 for _ in range(0, X*3)]

for i in range(2, X+1):
    dp[i] = dp[i-1] + 1
    if (i % 2 == 0):
        dp[i] = min(dp[i // 2] + 1, dp[i])
    if (i % 3 == 0):
        dp[i] = min(dp[i // 3] + 1, dp[i])
    # for rep in range(3):
    #     if rep == 1:
    #         if(i*2> X): continue;
    #         if(dp[i * 2] and dp[i * 2] > dp[i]+1):
    #             dp[i * 2] = dp[i]+1
    #         elif (dp[i * 2] == 0):
    #             dp[i * 2] = dp[i]+1
    #     elif rep == 2:
    #         if (i * 3 > X): continue;
    #         if (dp[i * 3] and dp[i * 3] > dp[i]+1):
    #             dp[i * 3] = dp[i] + 1
    #         elif (dp[i * 3] == 0):
    #             dp[i * 3] = dp[i]+1
    #     else:
    #         if (i + 1 > X): continue;
    #         if (dp[i + 1] and dp[i + 1] > dp[i]+1):
    #             dp[i + 1] = dp[i]+1
    #         elif (dp[i + 1] == 0):
    #             dp[i + 1] = dp[i]+1
print(dp[X])