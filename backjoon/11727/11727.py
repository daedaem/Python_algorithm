import sys
sys.stdin = open('11727.txt')

n = int(input())

ans = [0 for _ in range(17+1)]
# print(ans)
ans[0] = 0
ans[1] = 1
ans[2] = 3
def nemo(n):
    for i in range(3, n+1):
        if i % 2 == 1:
            ans[i] = ( 2* ans[i-1]) - 1
        if i % 2 == 0:
            ans[i] = (2 * ans[i-1]) + 1
nemo(17)
# print(ans)
# print(ans[17])
# print(ans[17])
print(ans[n] % 10007)