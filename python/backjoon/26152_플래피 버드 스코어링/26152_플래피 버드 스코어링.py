import sys
sys.stdin = open("26152_txt")

# def binarySearch(birdS):
#     start = 0
#     end = N-1
#     maxidx = 0
#     while(start<=end):
#         mid = (start+end)//2
#         if newarr[mid][0] >= birdS:
#             start = mid+1
#             if maxidx < mid:
#                 maxidx = mid
#             else:
#                 return maxidx
#         else:
#             end = mid-1
#     return maxidx


N = int(input())
upside = list(map(int, input().split()))
downside = list(map(int, input().split()))
newarr=[]
for i in range(N):
    newarr.append(upside[i]-downside[i])
# newarr.sort()

birdCnt = int(input())
birdSize = list(map(int, input().split()))
print(newarr)
answer= []
for i in range(birdCnt):
    if i==0:
    else:
        answer[i-1]
    # print(binarySearch(birdSize[i]))


