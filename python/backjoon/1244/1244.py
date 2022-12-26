import sys
sys.stdin = open('1244.txt')
# 스위치 갯수
N = int(input())
if N < 20:
    # numswi = list(map(int, range(1, N+1)))
    # 스위치 상태 인덱스 안 헷갈리게 걍 앞에 0붙이고 나중에 맨 앞만 없애자
    status = [0] + list(map(int, input().split()))
    # 학생수
    stnum = int(input())
    # 학생 정보 2차원 배열 [i][j] i는 번째 학생 j는 0이면 성별 1이면 스위치 번호
    st_info = [list(map(int, input().split())) for _ in range(stnum)]

    for i in range(stnum):
        # 남학생이면
        if st_info[i][0] == 1:
            # 순번이 남학생의 수로 나누어 떨어진다면
            for j in range(1, N + 1):
                # 스위치의 상태를 바꿔준다. 시간초과라면 if 말고 not으로 해결해도 좋을듯
                if j % st_info[i][1] == 0:
                    if status[j] == 1:
                        status[j] = 0
                    else:
                        status[j] = 1
                else:
                    pass
        # 여학생이면
        else:  # 오류나면 elif st_info[i][0] == 2:로 교체
            # 1을 받았으면 st_info[i][0]을 index에 받고 인덱스로해서 status[index-i]== status[index+i] 지속되면 해당 부분 교체
            # 대신 index-i == o이나 index+i == N보다 안크게
            index = st_info[i][1]
            # 먼저 해당 스위치 부터 바꾸기
            if status[index] == 0:
                status[index] = 1
            else:
                status[index] = 0
            # 다음 좌우로 대칭이 안될때까지 교체
            for i in range(1, N + 1):
                if index - i < 0 or index + i > N:
                    pass
                else:
                    while status[index - i] == status[index + i]:
                        if status[index - i] == 0:
                            status[index - i], status[index + i] = 1, 1
                            break
                        else:
                            status[index - i], status[index + i] = 0, 0
                            break
    print(status[1:N + 1])
elif N > 20:
    # 스위치 갯수
    # numswi = list(map(int, range(1, N+1)))
    # 스위치 상태 인덱스 안 헷갈리게 걍 앞에 0붙이고 나중에 맨 앞만 없애자
    status = [list(map(int, input().split())) for i in range((N // 20)+1)]
    print(status)
    # # 학생수
    # stnum = int(input())
    # # 학생 정보 2차원 배열 [i][j] 인덱스i는 i번째 학생 j==0 성별정보, j==1 스위치 번호
    # st_info = [list(map(int, input().split())) for _ in range(stnum)]
    #
    # for i in range(stnum):
    #     # 남학생이면
    #     if st_info[i][0] == 1:
    #         # 순번이 남학생의 수로 나누어 떨어진다면
    #         for j in range(1, N + 1):
    #             # 스위치의 상태를 바꿔준다. 시간초과라면 if 말고 not으로 해결해도 좋을듯
    #             if j % st_info[i][1] == 0:
    #                 if status[j] == 1:
    #                     status[j] = 0
    #                 else:
    #                     status[j] = 1
    #             else:
    #                 pass
    #     # 여학생이면
    #     else:  # 오류나면 elif st_info[i][0] == 2:로 교체
    #         # 1을 받았으면 st_info[i][0]을 index에 받고 인덱스로해서 status[index-i]== status[index+i] 지속되면 해당 부분 교체
    #         # 대신 index-i == o이나 index+i == N보다 안크게
    #         index = st_info[i][1]
    #         # 먼저 해당 스위치 부터 바꾸기
    #         if status[index] == 0:
    #             status[index] = 1
    #         else:
    #             status[index] = 0
    #         # 다음 좌우로 대칭이 안될때까지 교체
    #         for i in range(1, N + 1):
    #             if index - i < 0 or index + i > N:
    #                 pass
    #             else:
    #                 while status[index - i] == status[index + i]:
    #                     if status[index - i] == 0:
    #                         status[index - i], status[index + i] = 1, 1
    #                         break
    #                     else:
    #                         status[index - i], status[index + i] = 0, 0
    #                         break
    # print(status[1:N + 1])
