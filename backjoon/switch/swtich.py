import sys
sys.stdin = open('switch.txt')
N = int(input())
# numswi = list(map(int, range(1, N+1)))
# 스위치 상태 인덱스 안 헷갈리게 걍 앞에 0붙이고 나중에 맨 앞만 없애자
status = list(map(int, input().split()))  ####
# print(status)
# 학생수
stnum = int(input())
# 학생 정보 2차원 배열 [i][j] i는 번째 학생 j는 0이면 성별 1이면 스위치 번호
st_info = [list(map(int, input().split())) for _ in range(stnum)]

for i in range(stnum):
    # 남학생이면
    if st_info[i][0] == 1:
        # 순번이 남학생의 수로 나누어 떨어진다면
        for j in range(st_info[i][1] - 1, N, st_info[i][1]):  ####
            # 스위치의 상태를 바꿔준다. 시간초과라면 if 말고 not으로 해결해도 좋을듯
            if status[j] == 1:
                status[j] = 0
            else:
                status[j] = 1
    # 여학생이면
    else:  # 오류나면 elif st_info[i][0] == 2:로 교체
        # 1을 받았으면 st_info[i][0]을 index에 받고 인덱스로해서 status[index-i]== status[index+i] 지속되면 해당 부분 교체
        # 대신 index-i == o이나 index+i == N보다 안크게
        index = st_info[i][1] - 1
        # 먼저 해당 스위치 부터 바꾸기
        if status[index] == 0:
            status[index] = 1
        else:
            status[index] = 0

        i = 1
        while 0 <= index - i and index + i < N and status[index - i] == status[index + i]:
            if status[index - i] == 0:
                status[index - i], status[index + i] = 1, 1
            else:
                status[index - i], status[index + i] = 0, 0
            i += 1

if N <= 20:
    print(*status)
else:  # 22
    x = N // 20
    for i in range(0, x + 1):
        # z = status[20*i+1 : 20*(i+1)+1]
        print(*(status[20 * i: 20 * (i + 1)]))



# # 1번 받은 리스트의 인덱스 0이 남자 1이면
# # 그 리스트의 인덱스 1번 값 3이면
# #  스위치 번호와 상태 리스트로 받아 놓고
# # 스위치 번호 //3 ==0이면 안에 if 두번걸어서 0이면 1로 1이면 0으로
#
# # 그 담번 리스트의 인덱스 0이 여자 2이면
# # 그 리스트 인덱스 1의 값을 스위치번호에서 대입하여
# # for i range(1,)를 통해 스위치 번호 + i == 스위치 번호 -1 이면 스위치 상태 변화 시켜준다.
# import sys
# sys.stdin = open('switch.txt')
# # 스위치 갯수
# N = int(input())
# # numswi = list(map(int, range(1, N+1)))
# # 스위치 상태 인덱스 안 헷갈리게 걍 앞에 0붙이고 나중에 맨 앞만 없애자
# status = list(map(int, input().split()))
# # 학생수
# stnum = int(input())
# # 학생 정보 2차원 배열 [i][j] i는 번째 학생 j는 0이면 성별 1이면 스위치 번호
# st_info = [list(map(int, input().split())) for _ in range(stnum)]
# print(st_info)
# for i in range(stnum):
#     if st_info[i][0] == 1:
#         for j in range(1, N):
#             if j % st_info[i][1] == 0:
#                 if status[j] == 1:
#                     status[j] = 0
#                 if status[j] == 0:
#                     status[j] = 1
#
# # 여학생이면
#     else:  # 오류나면 elif st_info[i][0] == 2:로 교체
#         # 1을 받았으면 st_info[i][0]을 index에 받고 인덱스로해서 status[index-i]== status[index+i] 지속되면 해당 부분 교체
#         # 대신 index-i == o이나 index+i == N보다 안크게
#         index = st_info[i][1]
#         # 먼저 해당 스위치 부터 바꾸기
#         if status[index-1] == 0:
#             status[index-1] = 1
#         if status[index-1] == 1 :
#             status[index-1] = 0
#         # 다음 좌우로 대칭이 안될때까지 교체
#         for i in range(1, N):
#             if index-1 - i < 0 or index-1 + i > N-1:
#                 break
#             else:
#                 while status[index-1 - i] == status[index-1 + i]:
#                     if status[index-1 - i] and status[index-1 + i] == 0:
#                         status[index-1 - i], status[index-1 + i] = 1, 1
#                     if status[index - 1 - i] and status[index - 1 + i] == 1:
#                         status[index-1 - i], status[index-1 + i] = 0, 0
# if N <= 20:
#     print(*(status[:N + 1]))
# else: # 22
#     x = N//20
#     for i in range(0, x+1):
#         # z = status[20*i+1 : 20*(i+1)+1]
#         print(*(status[20*i : 20*(i+1)]))
#
#
#
# # for i in range(stnum):
# #     # 남학생이면
# #     if st_info[i][0] == 1:
# #         # 순번이 남학생의 수로 나누어 떨어진다면
# #         for j in range(1, N + 1):
# #             # 스위치의 상태를 바꿔준다. 시간초과라면 if 말고 not으로 해결해도 좋을듯
# #             if j % st_info[i][1] == 0:
# #                 if status[j] == 1:
# #                     status[j] = 0
# #                 else:
# #                     status[j] = 1
# #             else:
# #                 pass
# #     # 여학생이면
# #     else:  # 오류나면 elif st_info[i][0] == 2:로 교체
# #         # 1을 받았으면 st_info[i][0]을 index에 받고 인덱스로해서 status[index-i]== status[index+i] 지속되면 해당 부분 교체
# #         # 대신 index-i == o이나 index+i == N보다 안크게
# #         index = st_info[i][1]
# #         # 먼저 해당 스위치 부터 바꾸기
# #         if status[index] == 0:
# #             status[index] = 1
# #         else:
# #             status[index] = 0
# #         # 다음 좌우로 대칭이 안될때까지 교체
# #         for i in range(1, N + 1):
# #             if index - i <= 0 or index + i > N:
# #                 break
# #             else:
# #                 while status[index - i] == status[index + i]:
# #                     if status[index - i] == 0:
# #                         status[index - i], status[index + i] = 1, 1
# #                         break
# #                     else:
# #                         status[index - i], status[index + i] = 0, 0
# #                         break
# # if N <= 20:
# #     print(*(status[1:N + 1]))
# # else: # 22
# #     x = N//20
# #     for i in range(0, x+1):
# #         # z = status[20*i+1 : 20*(i+1)+1]
# #         print(*(status[20*i+1 : 20*(i+1)+1]))
#
#
#
#
