import sys
sys.stdin = open('1244.txt')

# 불 갯수
light_count = int(input())
# 불 상태
light_list = list(map(int, input().split())) #난중에 맨 앞만 슬라이싱
#학생 수
people_number = int(input())
# 학생 정보
people_list = [list(map(int, input().split())) for _ in range(people_number)]
#성별 확인
for i in range(people_number):
     #남자일때,
    if people_list[i][0] == 1:
        # 주어진 숫자의 배수가 불 인덱스번호라면 그 번호 불의 상태 변화
        for light_index in range(light_count):
            # print(light_list)
            # print(light_index)
            if (light_index+1) % people_list[i][1] == 0:
                if light_list[light_index] == 0:
                    light_list[light_index] = 1
                else:
                    light_list[light_index] = 0
            else:
                pass
            # print(light_list)
    else: #여자일때,
        if people_list[i][0] == 2:
        # 자기자신, 앞뒤 확인해줄 인덱스 cnt
            cnt = 0
            # 자기 자신 인덱스로 찾아야하니 -1
            center = people_list[i][1]-1
        ######밑에 or 때문에 인덱스 오류
            while center+cnt < light_count and center-cnt >= 0 :
                 if light_list[center+cnt] == light_list[center-cnt]:
                     if light_list[center + cnt] and light_list[center - cnt] == 1:
                         light_list[center+cnt], light_list[center-cnt] = 0, 0
                     else:
                         light_list[center+cnt], light_list[center-cnt] = 1, 1
                 else:
                    break
                 cnt+=1

#             if lightnumber != 0 and lightnumber % people_list[i][1] == 0:
#                 # print(lightnumber)
#                 # print(light[lightnumber])
#                 if light[lightnumber] == 0:
#                     light[lightnumber] = 1
#                 else:
#                     light[lightnumber] = 0
#             else:
#                 pass
#         # print(light[1:])
#     elif people_list[i][0] == 2:
#         cnt = 0
#         center = people_list[i][1]
#         # print(center)
#         while center-cnt >= 1 and center+cnt <= people_number+1:
#             if light[center-cnt] != light[center+cnt]:
#                 break
#             elif light[center-cnt] == light[center+cnt]:
#                 if light[center-cnt] == 1:
#                     light[center-cnt], light[center+cnt] = 0, 0
#                 elif light[center-cnt] == 0:
#                     light[center - cnt], light[center+cnt] = 1, 1 #뒷 부분 안넣어줘서 30분 헤맴
#             cnt += 1
#             # print(light[1:])
# lights = light[1:]
# result=[]
# print(lights)
##20개씩 출력에서 많은 시간을 소비
# 39개면 2줄 안에서 1
# 21개면 2줄 L1
# 1,L

L = light_count // 20 #21->1, L:2 1 #39 ->2 1, 1
if light_count > 20:
    for n in range(1, L+1):
        result = []
        ######## n*20 -1때문에 계속 틀림
        for i in range(20*(n-1), n*20):
            # result += [lights[i]]
            print(light_list[i], end=' ')
        print()
    for j in range(L*20, light_count):
        print(light_list[j], end=' ')
            # print(lights[i], end=' ')
        # print()
else:
    print(*light_list, end=' ')
#
#
#
