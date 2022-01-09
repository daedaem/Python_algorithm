import sys
sys.stdin = open('1699.txt')
N = int(input())
# ans는 기록
ans = [False] * (N+2)
# result = []
# a = 0
ans[1]=1
ans[2]=2
# min_value = N
vote = list(range(2, int(N ** (1/2))+1))[::-1]

def make_min(x):
    x = int(x **(1/2))
for i in vote:
    x = N - (i**2)
    while ans[x] == False:
        make_min(x)




def find(x):
    y = x - int(x ** (1/2))
    if ans[y] == False:
        find(y)
    else:
        for i in range(y):
            ans[x] = 1 + ans[i]

# def make_dp(x):
#     global min_value
#     min_value = N
#     for i in range(2, N):
#         min_value = N
#         for j in vote:
#             x = N - j ** 2
#             if ans[x] == False:
#                 find(x)
#             else:
#                 if min_value >= 1 + ans[x]:
#                     min_value = 1 + ans[x]
#             ans[i] = min_value
#     # ans[x] = make_dp(x)
#     # for i in range(1, N+1):
#     #     ans[x] = min_value
#
# make_dp(1)
# for j in vote:
#     ans[j ** 2] = 1
#
# result = []
# temp = []
# nam = 2
# # while nam > 1:
#     # for j in vote:
#         # nam-j
#
# # def find_min(x):
# #     if
#
#     # print(ans)
# print(min_value)
# for i in range(1, N):
#     dp(i)

# def find_x(x):
#     while x**2 < N:
#         ans.append(x)
#         x+=1
#
# def
# while a!= 0:
#     find_x(a)
# print(vote)
# print(result)

