import sys
sys.stdin=open('2798.txt')

N, M = map(int, input().split())
# print(N,M)
cards=list(map(int, input().split()))
# print(cards)
sums = []
for i in range(N-2):
    for j in range(i+1, N-1):
        for z in range(j+1, N):
            # print(cards[i], cards[j], cards[z])
            if cards[i]+cards[j]+cards[z] <= M:
                sums.append(cards[i]+cards[j]+cards[z])
print(max(sums))
######## 끝 #########

#
# 1.
# 3중 포문으로 고른 카드합과
# min = 21 차이의 절대값

# M//3 777
# 2.
# M//3
# sort해서 7과 차이의 절대값과 가장 작은 3개순위를 출력