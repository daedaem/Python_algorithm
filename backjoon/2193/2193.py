import sys
sys.stdin=open('2193.txt')

N = int(input())
# visite
ans = [False] * (90+1)
ans[1] = 1
ans[2] = 1

def dp(x):
    if ans[x] != False:
        return ans[x]
    else:
        ans[x] = dp(x-2) + dp(x-1)
        return ans[x]
dp(N)
print(ans[N])
# # 1 1
# 1   1   0 1     1
#
# 10  2   1 0     1
#
# 100 3   1 1     2
# 101
#
# 1000    4   2 1 3
# 1001
# 1010
#
# 10000   5   3 2 5
# 10001
# 10010
# 10100
# 10101
#
# 100000  6   5  3    8
# 100001
# 100010
# 100100
# 100101
# 101000
# 101001
# 101010
#
# 1000000     8 5 13
# 1000001
# 1000010
# 1000100
# 1001001
# 1001000
# 1001001
# 1001010
# 1010000
# 1010001
# 1010010
# 1010100
# 1010101
# # 2 1
# # 3 2
# 4 3
# 5 5
# 6 8
# 7 11