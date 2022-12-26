import sys
sys.stdin = open('1904.txt')
sys.setrecursionlimit(10**9)
N = int(input())
ans = [False for _ in range(N+1)]
ans[1]=1
ans[2]=2
x=1
# def dp(x):
#     if ans[x] != False or x < 3:
#         return ans[x]
#     ans[x] = (dp(x-1)%15746 + dp(x-2)%15746)
#     return ans[x]
while x <= N:
    if x <=2 :
        x +=1
        pass
    else:
        ans[x] = (ans[x-2] + ans[x-1])%15746
        x += 1
print(ans[N])


# dp(N)
# print(ans[N])
# def dp(x):
#     if ans[x] != False:
#         return ans[x]
#     else:
#         ans[x] = dp(x-1) + dp(x-2)
#         return ans[x]
# def dp(x):
#     if ans[x] or x < 3:
#         return ans[x]
#     else:
#         for i in range(3, x+1):
#             if ans[i] == False:
#                 ans[i] = dp(i-2) + dp(i-1)
#             else:
#                 return ans[i]
#     return ans[N]
# print(dp(N)%15746)
# print(ans[N]%15746)