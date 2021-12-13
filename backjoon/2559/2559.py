import sys
sys.stdin = open('2559.txt')

# import time
# startTime = time.time()
# 1. k개 만큼일단 맨 앞에서 더해놓고 bigvalue라는 변수에 저장
# 2. 그다음 맨 앞 값 빼고 뒤 값 더해서 sum
N, K = list(map(int, input().split()))
templist = list(map(int, input().split()))
templist_sum = 0
temp = []
# 일단 첫번째 k까지 합 구하고
for i in range(K):
    temp += [templist[i]]
templist_sum += sum(temp)
# print(templist_sum)
# 이제부터 맨앞 숫자 빼고(이전숫자)
for i in range(K, N):
    temp.remove(templist[i-K])
    temp += [templist[i]]
    if sum(temp) > templist_sum:
        templist_sum = sum(temp)
print(templist_sum)
#
#     maxs += [temp]
# print(max(maxs))

# endTime = time.time() - startTime
# print(endTime)
# N, K = list(map(int, input().split()))
# templist = list(map(int, input().split()))
# maxs = 0
# for i in range(N-K):
#     temp = 0
#     for j in range(K):
#         temp += templist[i+j]
#     if temp > maxs:
#         maxs = temp


