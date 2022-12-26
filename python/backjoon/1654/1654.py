import sys
sys.stdin = open('1654.txt')

def findMaxLen(length):
    cnt=0
    for num in lans:
        cnt += (num//length)
    if cnt >= K:
        return 1
    else:
        return 0

N , K = map(int,input().split())
lans = [int(input()) for _ in range(N)]

start = 1
end = max(lans)
maxLength = 0

while start <= end:
    mid = (start+end)//2
    ret = findMaxLen(mid)
    if ret and (maxLength < mid):
        maxLength = mid
        start = mid+1
    if not ret:
        end = mid-1

print(maxLength)