import sys
sys.stdin=open('2303.txt')

# print(chr(65))
# people = []
N = int(input())
# for i in range(x):
#     people += [chr(65+i) ]
# print(people)
# people = [chr(65)]
people = [list(map(int, input().split())) for _ in range(N)]
# print(people)
# print(A, B, C)
cnt=0

cards = [[0] for _ in range(len(people))]
temp = []
# 사람 수 반복문으로 각 사람 마다 카드 뽑기
for c in range(len(people)):
    temp = []
    for i in range(5):
        for j in range(i + 1, 5):
            for z in range(j + 1, 5):
                temp = (people[c][i]+people[c][j]+people[c][z])% 10
                cards[c] += [temp]
# 가장 큰 값 집어 넣기
# print(cards)
for i in range(len(cards)):
    cards[i] = max(cards[i])
maxvalue = 0
maxidx = 0

# maxidx = cards.index(max(cards))
# print(cards)
# print(maxidx+1)
cards = [9, 9, 9]
for i in range(len(cards)):
    # print(i)
    if maxvalue <= cards[i]:
        maxvalue = cards[i]
        # print(maxvlaue)
        maxidx = i

print(maxidx+1)

# print(maxidx+1)





# print(a, b, c)
#
# for i in range(5):
#     for j in range(i+1, 5):
#         for z in range(j+1, 5):
#             cnt +=1
#             a.append((A[i] + A[j] + A[z])&10)
#             b.append((B[i] + B[j] + B[z])&10)
#             c.append((C[i] + C[j] + C[z])&10)
# a, b, c = (max(a), max(b), max(c))
# result = [a, b, c]
# print(result)
# if a == b:
#     print(2)
# elif a == c:
#     print(3)
# elif b == c:
#     print(3)
# elif a== b == c:
#     print(3)
# else:


