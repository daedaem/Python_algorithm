import sys
sys.stdin = open('2628.txt')
# 리스트에 두개로 나누어서 될 수 있는 x값 leftm\, y값 right append해서 다 곱해보고 비교해보자

# 총 종이의 가로 x와 세로 y받기
x, y = list(map(int, input().split()))
# print(x, y)
# 잘라야하는 횟수 N
N = int(input())
metho= [list(map(int, input().split())) for _ in range(N)]
listy= []
listx= []
# metho[i][0]=0이면 가로로 자르니까 y축 부분, 1이면 x축 부분
# print(metho)
for i in range(N):
    if metho[i][0] == 0:
        listy.append(metho[i][1])
    else:
        listx.append(metho[i][1])
# print(listy)
# print(listx)
listx.append(0)
listx.append(x)
listy.append(0)
listy.append(y)
lenlistx=len(listx)
lenlisty=len(listy)
# 정렬한다 내림차순으로
for i in range(len(listx)-1): #3 i 01
    for j in range(len(listx)-1-i):
        if listx[j] > listx[j+1]:
            listx[j], listx[j + 1] = listx[j + 1], listx[j]
for i in range(len(listy)-1):
    for j in range(len(listy)-1-i):
        if listy[j] > listy[j+1]:
            listy[j], listy[j + 1] = listy[j + 1], listy[j]
# print(listx)
# print(listy)

listx.append(0)
#x값 y값 경우 다 넣는다
# for i in range(lenlistx):
newlistx = []
newlisty = []
for i in range(lenlistx-1):
    result = listx[i] - listx[i+1]
    newlistx.append(result)
for i in range(lenlisty-1):
    result = listy[i] - listy[i+1]
    newlisty.append(result)
# print(newlistx)
# print(newlisty)
result = 0
for i in newlistx:
    for j in newlisty:
        if result< i*j:
            result = i*j
print(result)
# 아~~~~~~~~~~~~~~~~~ 제일 큰거 곱하면 되겠구만