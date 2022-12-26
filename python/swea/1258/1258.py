import sys
sys.stdin = open('1258.txt')

tc = int(input())

# for index in range(1, tc+1):
n = int(input())
bigbox = [list(map(int, input().split())) for _ in range(n)]
record = [[0] * n for _ in range(n)]
# 상 하 좌 우
x = [0, 0, -1, 1]
y = [1, -1, 0, 0]
#
for i in range(n):
    for j in range(n):
        for z in range(4):
            if bigbox[i][j] != 0:
                record[i][j] = [i+1, j+1]
print(record)
vowl = []
for i in range(n):
    for j in range(n):
        if record[i][j] !=0:
            vowl.append(record[i][j])
print(vowl)

xvalues = []
yvalues = []
for i in range(len(vowl)):
    if vowl[i][0]== vowl[i+1][0]:
        vowl[i]

# #
# for tc in range(1, int(input()) + 1):
#     listt = []
#     N = int(input())
#     for in range(N):
#         list_t.append(list(map(int, input().split())))
#
#     list_count = [0](N + 1)
#     for i in range(N):
#         count = 0
#         for j in range(N):
#             if list_t[i][j] != 0:
#                 count += 1
#             elif list_t[i][j] == 0 and count != 0:
#                 list_count[count] += 1
#                 count = 0
#         if count != 0:
#             list_count[count] += 1
#
#     result = []
#     for idx, x in enumerate(list_count):
#         if x:
#             result.append([x, idx])
#     result.sort(key=lambda x: (x[0]x[1], x[0]))
#     print("#{} {}".format(tc, len(result)), end=" ")
#     for i in result:
#         for j in i:
#             print(j, end=" ")
#
#     print("")