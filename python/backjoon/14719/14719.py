import sys
sys.stdin = open('14719.txt')

H, W = list(map(int,input().split()))
# print(H,W)
world = list(map(int,input().split()))
# print(world)
end_value = 0
end_point = 501
for i in range(len(world)):
    if world[i] !=0:
        start_value = world[i]
        start_point = i
        break
# STD_value = start_value
# STD_point = start_point
result = 0
cnt = start_point
while cnt < len(world):
    for j in range(len(world[start_point:])):
        cnt+=1
        # 만약 같은 높이면 스타트지점 바꿔주기
        if world[start_point:][j]>=start_value:
            # 현재 있는 곳에서 머물지 않도록
            if start_point == j and start_value == world[start_point:][j]:
                # 한번 더 머물렀으니까 빼주기
                cnt-=1
                # print(cnt)
            else:
                # 같은 지점이 아닌데도 값이 같다면 시작지점을 바꿔서 다시
                start_point = j
                start_value = world[start_point:][j]
                break
        else:
            if cnt == len(world):
                if start_value > world[cnt]:
                    result -=(start_value - world[cnt]) * (len(world[start_point:])+2)
                break
            elif world[cnt]==0:
                result -=len(world[start_point:] *(start_value-world[start_point:][j]))
            else:
                result += start_value-world[start_point:][j]
    if cnt >= len(world):
        break
# print(cnt)
print(result)
# for i in range(len(world)):
# while world:

#     if world[i] == start_value:
#         start_point = i
#         start_value = world[i]
#     elif world[i] < start_value:
#     if world[i] > start_value and i-start_point!=1 :
#         start_value = world[i]
#         start_point = i
#     elif world[]
# for i in range(len(world)):
#     while world[i] == 0:
#         pass
#     start_value = world[i]
#     start_point = i
#     while world:
#         if end_point > len
#         for j in world[start_point:]:
#             if j>= start_value:
#                 if j-i ==1:
#                     start_value= world[j]
#                     start_point = j
#                 start_point = end_point = j
#                 start_value = end_value = world[j]
#                 break
#             else:
#                 result += start_value-j




#     if i == 0:
#         if world[i]!=0:
#             start_point=i
#             start_value = world[i]
#     else:
#         while start_value
#
#     if world[i] !=0 and :
#         start_point = i
#         start_value = world[i]
#         break
#     else:
#         pass
# print(start_point)
# print(start_value)

# result = 0
# while end_point:
#     for i in range(start_point, len(world)):
#         # print(i)
#         # i가 시작지점과 같지 않고 시작값보다 크다면
#         if i > start_point and world[i] >= start_value:
#             if i-start_point ==1:
#                 start_point = i
#                 start_value = world[i]
#             else:
#                 end_point = i
#                 end_value = world[i]
#                 for i in world[start_point:end_point]:
#                     result += start_value-world[i]
#                 start_value = end_value
#                 start_point = end_point
#         elif i > start_point and world[i] < start_value:
#             pass
# print(result)



    # while STD >= start:



