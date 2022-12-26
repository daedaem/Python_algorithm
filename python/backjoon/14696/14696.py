import sys
sys.stdin=open('14696.txt')

ROUND = int(input())
total = [list(map(int, input().split()))[1:] for _ in range(ROUND*2)]
# print(total)
A = []
B = []
for i in range(len(total)):
    if i %2:
        B.append(total[i])
    else:
        A.append(total[i])
print(A)
print(B)
result = []
vitory=0
for i in range(ROUND):

    if A[i].count(4) > B[i].count(4):
        victory = 'A'
    if A[i].count(4) < B[i].count(4):
        victory = 'B'
    if A[i].count(4) == B[i].count(4) and A[i].count(3) > B[i].count(3):
        victory = 'A'
    if A[i].count(4) == B[i].count(4) and A[i].count(3) < B[i].count(3):
        victory = 'B'
    if A[i].count(4) == B[i].count(4) and A[i].count(3) == B[i].count(3) and A[i].count(2) > B[i].count(2):
        victory = 'A'
    if A[i].count(4) == B[i].count(4) and A[i].count(3) == B[i].count(3) and A[i].count(2) < B[i].count(2):
        victory = 'B'
    if A[i].count(4) == B[i].count(4) and A[i].count(3) == B[i].count(3) and A[i].count(2) == B[i].count(2)and A[i].count(1) > B[i].count(1):
        victory = 'A'
    if A[i].count(4) == B[i].count(4) and A[i].count(3) == B[i].count(3) and A[i].count(2) == B[i].count(2) and A[i].count(1) < B[i].count(1):
        victory = 'B'
    if A[i].count(4) == B[i].count(4) and A[i].count(3) == B[i].count(3) and A[i].count(2) == B[i].count(2) and A[i].count(1) == B[i].count(1):
        victory = 'D'
    result.append(victory)
print(*result)

#     # if A[i].count(1) > B[i].count(1):
#     # elif A[i].count(1) < B[i].count(1):
#     #
#     #     if A[i].count(2) > B[i].count(2):
#     #         if A[i].count(3) > B[i].count(2):
#     #             if A[i].count(4) > B[i].count(4):
#     #                 victory = 'A'
#     #             elif A[i].count(4) < B[i].count(4):
#     #                 victory = 'B'
#     #         elif A[i].count(3) < B[i].count(2):
#     #             if A[i].count(4) > B[i].count(4):
#     #                 victory = 'A'
#     #             elif A[i].count(4) < B[i].count(4):
#     #                 victory = 'B'
#     #         else:
#     #             if A[i].count(2) < B[i].count(2):
#     #                 result.append('B')
#     #     else:
#     #         A[i].count(1) > B[i].count(1):
#     #         result.append('B')
#     # if A[i].count(1) < B[i].count(1):
#     #     result.append('B')
#     #     if A[i].count(2) > B[i].count(2):
#     #         result.append('A')
#     #     else:
#     #         A[i].count(1) > B[i].count(1):
#     #         result.append('B')