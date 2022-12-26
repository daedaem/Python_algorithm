import sys
sys.stdin = open('2477.txt')
# 땅 1미리제곱당 참외개수 K
K = int(input())
# 땅 길이
ground_info = [list(map(int, input().split())) for _ in range(6)]
# print(ground_info)
# 반복되는게 있음 423131(01 2345) 231314(0 1234 5) 313142(0123 45) 131423(012 34 5, 02 15) 314231(01 23 45, 04 15) 142313(0 12 345, 04 35 )
# 겹치는게 2개면 해결 232314 12 313142 231314  423131   0123 1234 2345 3456 423131
double_num = []
 # 231314  313142   423131    1 3 2 4        1 3 0 2     0 1 2 3 4

i = 2
# 423131(01 2345)
if ground_info[i][0] == ground_info[i+2][0] and ground_info[i+1][0] == ground_info[i+3][0]:
    x = ground_info[i+1][1]
    y = ground_info[i+2][1]
    double_num.append([ground_info[i+3][1], x])
    double_num.append([ground_info[i][1], y]) #
# 231314(0 1234 5)
if ground_info[i-1][0] == ground_info[i + 1][0] and ground_info[i][0] == ground_info[i + 2][0]:
    x = ground_info[i + 1][1]
    y = ground_info[i][1]
    double_num.append([ground_info[i-1][1], x])
    double_num.append([ground_info[i+2][1], y])#
# 3142(0123 45)
if ground_info[i-2][0] == ground_info[i][0] and ground_info[i-1][0] == ground_info[i + 1][0]:
    x = ground_info[i][1]
    y = ground_info[i-1][1]
    double_num.append([ground_info[i-2][1], x])
    double_num.append([ground_info[i+1][1], y]) #
# 131423(012 34 5, 02 15)
if ground_info[i-2][0] == ground_info[i][0] and ground_info[i-1][0] == ground_info[i + 3][0]:
    x = ground_info[i-2][1]
    y = ground_info[i-1][1]
    double_num.append([ground_info[i][1], x])
    double_num.append([ground_info[i+3][1], y]) #
#  314231(01 23 45, 04 15)
if ground_info[i-2][0] == ground_info[i + 2][0] and ground_info[i-1][0] == ground_info[i + 3][0]:
    x = ground_info[i-2][1]
    y = ground_info[i + 3][1]
    double_num.append([ground_info[i + 2][1], x])
    double_num.append([ground_info[i-1][1], y]) #
#  142313(0 12 345, 04 35 )
if ground_info[i-2][0] == ground_info[i + 2][0] and ground_info[i + 1][0] == ground_info[i + 3][0]:
        x = ground_info[i + 2][1]
        y = ground_info[i + 3][1]
        double_num.append([ground_info[i-2][1], x])
        double_num.append([ground_info[i+1][1], y])

# 큰사각형넓이
bigsquare = sum(double_num[0]) * sum(double_num[1])
# print(bigsquare)

#작은사각형은 4242 이면 안에있는 2, 4의 길이곱한게 작은사각형 넓이
smallsquare = x * y
# print(smallsquare)
result = K*(bigsquare-smallsquare)
print(result)




# 랭킹 3위 미친 풀이
# n=int(input())
# x=[int(input().split()[1])for _ in range(6)]*2
# i=x.index(max(x))
# j=x.index(max(x[i-1],x[i+1]))
# print(n*(x[i]*x[j]-x[i+3]*x[j+3]))