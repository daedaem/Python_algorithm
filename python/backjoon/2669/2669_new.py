import sys
sys.stdin = open('2669.txt')

# 큰 좌표수 얻어서 큰 배열 만들고
# 가로 x축, y축에 맞게 +1

circle_list = [list(map(int, input().split())) for _ in range(4)]
# print(circle_list)
max =0
for i in range(4):
    for j in range(4):
      if circle_list[i][j] >= max:
          max= circle_list[i][j]
# print(max)
record = [[0] *(max+1) for _ in range((max+1))]
# print(record)
# x=0,2 y=1,3
x_list = []
y_list = []
# 0, 2번째 합치고 1,3 번째 합쳐서 다시 2차원배열
for i in range(4):
    circle_list[i][1], circle_list[i][2] = circle_list[i][2], circle_list[i][1]
# print(circle_list)

for i in range(4):
    for j in range(circle_list[i][0], circle_list[i][1]):
        for z in range(circle_list[i][2], circle_list[i][3]):
            record[j][z] += 1

result =0
for i in range(max+1):
    for j in range(max+1):
        if record[i][j] !=0:
            result+=1
print(result)
# if record[]
# print(record)





    # x_list.append([circle_list[i][0], circle_list[i][2]])
    # y_list.append([circle_list[i][1], circle_list[i][3]])
# print(x_list)
# print(y_list)

    # for j in range(0, 4, 2):
    #     lists.append([j, j+1])

