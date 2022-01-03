import sys
sys.stdin = open('back2669.txt')
T = 4
#사각형 x1, y1, x2, y2 정보 한줄당 하나

rect = [list(map(int, input().split())) for i in range(T)]
# print(rect) # react[1~4] 숫자에 따라 각 사각형 x1~ y2 정보 담김
onesquare_area = 0
# 1.하나도 안 겹친 사각형들의 넓이 구하자
for i in range(len(rect)):
    onesquare_area += (rect[i][2] - rect[i][0]) * (rect[i][3] - rect[i][1])
# print(onesquare_area)

# 1.사각형 두개 중 비교해서 겹치는 것 받자
# 1-1. 우선 겹치는 조건 확인 하자
# 조건
# x=1 [0] x2 [2] y1[1] y2[3]
#1. x축은 a x1이 b x1보다 작고 a x2가 b x1보다 크다
#1-1. y축은 a y1이 b y1보다 작고 a y2 b y1보다 큼
#1-2. y축 a y1이 b y1보다 크고 b의 y2보다 작다.
#2. a x1이 b x1보다 크고 a x2는 b x2보다 작거나 같거나 크다.
#2-1. y축은 a y1이 b y1보다 작고 a y2 b y1보다 큼
#2-2. y축 a y1이 b y1보다 크고 b의 y2보다 작다.
twosquare=[]
# 위 조건을 겹친 박스안에서도 똑같이
# y축은
for i in range(T):
    for j in range(i+1, 4):
        if rect[i][0] < rect[j][2] and rect[i][2] > rect[j][0]:
            if rect[i][0] < rect[j][1] and rect[i][3] > rect[j][1]:
                twosquare.append([rect[i], rect[j]])
            if rect[j][1] < rect[i][1] < rect[j][3]:
                twosquare.append([rect[i], rect[j]])
        elif rect[i][2] < rect[j][0] and rect[i][0] > rect[j][2]:
            if rect[i][1] < rect[j][1] and rect[i][3] > rect[j][1]:
                twosquare.append([rect[i], rect[j]])
            if rect[j][1] < rect[i][1] < rect[j][3]:
                twosquare.append([rect[i], rect[j]])
### 이까지 twosquare 는 겹친 사각형 목록들

# 1-2 가져온 변수에서 넓이를 구하자
# 면적들 구하자
# x1은 큰값 , x2는 작은거 y1은  큰거 y2는 작은거
twosquare_area =[]
newbox=[]
for i in range(len(twosquare)):
    new_x1 = max(twosquare[i][0][0], twosquare[i][1][0])
    new_x2 = min(twosquare[i][0][2], twosquare[i][1][2])
    new_y1 = max(twosquare[i][0][1], twosquare[i][1][1])
    new_y2 = min(twosquare[i][0][3], twosquare[i][1][3])
    area = (new_x2 - new_x1) * (new_y2 - new_y1)
    twosquare_area.append(area)
# print(sums)
### 이까지 sums는 겹치는 사각형들의 넓이들
    newbox.append([new_x1, new_y1, new_x2, new_y2])
# print(newbox)
### newbox는 겹치는 세박스

# 2, 세개 중 비교해서 겹치는건 두개 중 비교랑도 똑같네
# 세개 겹치는 것도 위에서 구한 박스에서 처리하자
newboxinfo= []
for i in range(len(newbox)):
    x1 = newbox[0][0]
    if x1 < newbox[i][0]:
        x1 = newbox[i][0]
newboxinfo.append(x1)
for i in range(len(newbox)):
    y1 = newbox[0][1]
    if y1 < newbox[i][1]:
        y1 = newbox[i][1]
newboxinfo.append(y1)
for i in range(len(newbox)):
    x2 = newbox[0][2]
    if  x2 > newbox[i][2]:
        x2 = newbox[i][2]
newboxinfo.append(x2)
for i in range(len(newbox)):
    y2 = newbox[0][3]
    if y2 > newbox[i][3]:
        y2 = newbox[i][3]
newboxinfo.append(y2)

### 이까지 newboxinfo는 세개 겹친 박스의 좌표들

###여기서 부터는 세개 겹친 사각형 넓이
newboxarea = (newboxinfo[2] - newboxinfo[0]) * (newboxinfo[3] - newboxinfo[1])
# print(newboxarea)

# 결론적으로 4사각형 합에서 2개 겹친 사각형합 빼주고 세개 겹친 사각형을 1번 더해주면 됌
result = onesquare_area - sum(twosquare_area) + newboxarea
print(result)
# 2.1

# 위 조건을 겹친 박스안에서도 똑같이


# # 면적은 이차원 배열에서 그 안에 각 0, 1, 2, 3에 해당하는
# # 1차원 리스트 안에 해당 사각형의 (idx0-2) * abs(idx1-3)
# ### x1 0 y1 1 x2 2 y2 3
# # 1. 2차원 배열을 순회할 맨 겉의 for문
# sums = 0
# for i in range(4):
#     for j in range(1):
#         result = (abs(rects[i][j] - rects[i][j+2])) * (abs(rects[i][j+1] - rects[i][j+3]))
#         sums += result
# print(sums)
# # 아래에서 진행할 직사각형 넓이들을 담을 sum변수
# # 그 안에서 1차원 배열의 각 콜럼을 비교할 for문
# # 구하고 나서 sum에 추가
#
# # 세개 겹치는 녀석
# # for i in range(3):
# #     for j in range(4):
# #         rect[]
# #
#
# # 일단 두개 사각형이라도 해보자
#
#
# # 0이 가장 큰거 x1, 2가 가장 가장 큰거 y1, 3가장 작은거 x2 y2는 가장 큰거
# # 겹치는거 해결
# # 세개 겹치는거 -2빼고 둘이서 겹치는거 하나씩
#
# # x1, 리스트[i]두개중  x좌표 큰값 y좌표 큰값
# # x2는 리스트 두개 중 3인덱스가 작은걸로
# # y1은 리스트 두개중 1인덱스가 큰걸로
# # y2는 ''중 작은걸로
# 1,2 4,4   3,2 4,4까지는 모두 겹친거       1~4 2~4
# 2,3 5,7   0과1은 2,3 4,4까지      2~5  3~7
# 3,1 6,5   0과 2는 3,2 4,4      3~6  3~5
#           1과 2는 3,3 5,5까지
# #
# 7,3 8,6         7~8  3~6