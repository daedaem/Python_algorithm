import sys
sys.stdin=open('13300.txt')

N, K = map(int, input().split())
people = [list(map(int, input().split())) for _ in range(N)]
# print(people)
# print(S, Y)
man = [0 for _ in range(7)]
# print(man)
woman = [0 for _ in range(7)]
for i in range(len(people)):
    # print(people[i][1])
    if people[i][0] == 1:
        man[people[i][1]] += 1
    if people[i][0] == 0:
        woman[people[i][1]] += 1
# print(man)
# print(woman)
result = 0
for i in range(len(man)):
    if man[i] != 0 and man[i] % K:
        result += man[i]//K+1
    if man[i] % K == 0:
        result += man[i]//K
    if woman[i] != 0 and woman[i] % K:
        result += woman[i]//K+1
    if woman[i] % K == 0:
        result += woman[i]//K
print(result)
