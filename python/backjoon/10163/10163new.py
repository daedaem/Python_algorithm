import sys
sys.stdin=open('10163.txt')

sums = 0
square_list = []

N = int(input())

records = [[-1]*1002 for _ in range(1002)]

squares_info = [list(map(int, input().split())) for _ in range(N)]
# print(squares_info)
# total_x_info = []
# total_y_info = []
for i in range(N):
    for j in range(squares_info[i][1], squares_info[i][1] + squares_info[i][3]):
        # print(j)
        for z in range(squares_info[i][0], squares_info[i][0] + squares_info[i][2]):
            records[j][z] = i
# print(records)
result = []
temp = 0
for z in range(N):
    for i in range(1002):
        for j in range(1002):
            if records[i][j] == z:
                temp += 1
    result.append(temp)
total = [result[0]]
for i in range(N-1):
    total.append(result[i+1]-result[i])
print(*total)
# print(result)
    # total_x_info.append([squares_info[i][0],squares_info[i][2]-squares_info[i][0]])