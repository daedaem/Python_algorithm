import sys
sys.stdin = open('1913.txt')

N = int(input())
find_number = int(input())
Y = [-1, 0, 1, 0]
X = [0, 1, 0, -1]

midde_y, midde_x = int(N/2), int(N/2)
# print(midde_y, midde_x)
table = [[0 for _ in range(N)] for _ in range(N)]
# print(table)
# for i in range(N):
cnt = 1
point = 0
table[midde_y][midde_x] = 1
# while point < 5 and cnt < find_number:
for j in range(1, int(N/2+1)):
    point = point % 4
    dy = midde_y + Y[point]
    dx = midde_x + X[point]
    if dy > N/2+j or dx > N/2+j or dy < N/2-j or dx < N/2-j:
        dy = midde_y - Y[point]
        dx = midde_x - X[point]
        point+=1
    else:
        # print(dy, dx)
        cnt+=1
        table[dy][dx] += cnt
print(table)





# for i in range()