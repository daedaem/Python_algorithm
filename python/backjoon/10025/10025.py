import sys
sys.stdin=open('10025.txt')

N, K = map(int, input().split())
# print(N, K)
arr = [list(map(int, input().split())) for _ in range(N)]
# print(arr)
max_value = 0
arr_len = 0

for i in range(N):
    if arr[i][1]>=arr_len:
        arr_len=arr[i][1]
record = [0] * 1000001
for i in range(N):
    record[arr[i][1]] = arr[i][0]
temp = 0
if arr_len <= 2*K:
    print(sum(record))
elif arr_len > 2*K:
    for i in range(2*K+1):
        max_value += record[i]
        temp += record[i]
    # print(max_value)
    # print(temp)
    for i in range(K, arr_len-K+1):
        # print(i)
        # print(record[i-K], record[i+K+1], temp)
        # temp=0
        # temp=0
        temp = temp - record[i-K]+record[i+K+1]
        # for j in range(i-K, i+K+1):
        if temp>= max_value:
            max_value=temp
    print(max_value)
