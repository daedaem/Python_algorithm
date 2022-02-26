import sys
sys.stdin = open("18111.txt")

N, M, B = map(int, input().split())
avg_ground =0
ground =[]
case1_b = B
case2_b = B

# ground = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    # for j in range(M):
    temp = list(map(int, input().split()))
    avg_ground += sum(temp)
    ground += [temp]
avg_ground = avg_ground /(N*M)
print(avg_ground)
print(ground)

case1 = int(avg_ground-1)
if case1 < 0:
    case1 = 0
case2 = int(avg_ground+1)
print(case1, case2)

result_1 = 0
result_2 = 0
for i in range(N):
    for j in range(M):
        # case1
        if case1 > ground[i][j]:
            result_1 += (case1 - ground[i][j])
            case1_b -= (case1 -ground[i][j])
        elif case1 < ground[i][j]:
            result_1 += (ground[i][j] - case1) *2
            case1_b += (ground[i][j]-case1)
        # case2
        if case2 > ground[i][j]:
            result_2 += (case2 - ground[i][j])
            case2_b -= (case2 -ground[i][j])
        elif case2 < ground[i][j]:
            result_2 += (ground[i][j] - case2) *2
            case2_b += (ground[i][j]-case2)
print(result_1, case1, case1_b)
print(result_2, case2, case2_b)

    # print(temp)

# print(list(temp))
# print(N, M, B)
# print(ground)
