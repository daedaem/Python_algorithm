import sys
sys.stdin = open('2304.txt')
N = int(input())
column_number = []
column_height = []
for _ in range(N):
    columns = list(map(int, input().split()))
    column_number += [columns[0]]
    column_height += [columns[1]]
# # 인덱스에 맞게 0으로 다 표시하자
# for index in range(1, N+1):
#     column_info = list(map(int, input().split()))
#     column_number.append(column_info[0])
#     column_height.append(column_info[1])
# print(column_number)
# print(column_height)
infos = (max(column_number)+1) * [0]
for i in range(N):
    num = column_number[i]
    heig = column_height[i]
    infos[num] = heig
# print(infos)
#
# # 일단 max값까지 꾸준히 올라갔다가
# # 그담 구간 max값 까지 쭉이어져 가는듯
max_infos_pos = infos.index(max(infos))
# #일단 맥스값 위치 max infos_pos 앞까지 앞전보다 작으면 교체계속
for i in range(1, max_infos_pos):
    if infos[i] < infos[i-1]:
        infos[i] = infos[i-1]
# # 뒤에서부터는 지금 내보다 작으면 나로 교체
for i in range(len(infos)-1, max_infos_pos, -1): #9까지
    if infos[i] > infos[i-1]:
        infos[i-1] = infos[i]
# print(infos)

newlist = [0] * (max(infos)+1)
# print(newlist)
for i in infos:
    newlist[i] += 1
result = 0
for i in range(len(newlist)):
    result += i * newlist[i]
print(result)