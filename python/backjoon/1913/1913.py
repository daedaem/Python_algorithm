import sys
sys.stdin = open('1913.txt')
# sys.stdout = open('output.txt','w')
N = int(input())
find_number = int(input())
Y = [-1, 0, 1, 0]
X = [0, 1, 0, -1]

mid_y, mid_x = int(N/2), int(N/2)
# print(midde_y, midde_x)
table = [[0 for _ in range(N)] for _ in range(N)]
# print(table)
# for i in range(N):
cnt = 1
point = 0
table[mid_y][mid_x] = 1
ans_2=[]
# while point < 5 and cnt < find_number:
for j in range(1, int(N/2)+1):
    # 1,2
    # 3 5
    # 1
    while cnt < (j*2+1)**2:
        point = point % 4
        # 0,1
        mid_y = mid_y + Y[point]
        mid_x = mid_x + X[point]
        # (-1,1)
        if mid_y > int(N/2)+j or mid_x > int(N/2)+j or mid_y < int(N/2)-j or mid_x < int(N/2)-j:
            # 2 2 0 0
            mid_y -= Y[point]
            mid_x -= X[point]
            point+=1
        else:
            # print(mid_y, mid_x)
            # print(dy, dx)
            cnt+=1
            if cnt == find_number:
                ans_2.append(mid_y+1)
                ans_2.append(mid_x+1)
            table[mid_y][mid_x] += cnt
    #         1,0 =2
# print(table)
for i in range(N):
    for j in range(N):
        print(table[i][j], end=" ")
    print()
if find_number ==1:
    print(int(N/2+1), int(N/2+1))
else:
    for i in ans_2:
        print(i, end= " ")

