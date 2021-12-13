import sys
sys.stdin = open('1244.txt')

switch_N = int(input())
switch_status = list(map(int, input().split()))
students_N=int(input())
students_status= [list(map(int,input().split())) for _ in range(students_N)]
# print(students_N)
# print(switch_status)
# print(students_status)

# 1은 on 0은 off
for i in range(students_N):
    # 남학생일 때,
    if students_status[i][0] == 1:
        # 스위치 번호가 자기 받은 수의 배수이면, 스위치 상태 변경
        for j in range(students_status[i][1]-1, switch_N, students_status[i][1]):
            if switch_status[j] == 0:
                switch_status[j] = 1
            else:
                switch_status[j] = 0
        # print(switch_status)
        # 01110101
    # 여학생일 때,
    elif students_status[i][0] == 2:
        # 자기 받은 수를 중심으로 좌우 대칭이면 변경
        # 자기자신 변경
        center = students_status[i][1] - 1
        if switch_status[center] == 1:
            switch_status[center] = 0
        else:
            switch_status[center] = 1
        # 자기 좌우로 대칭이면 변경
        cnt = 1
        while 0 <= center - cnt and center + cnt <= switch_N-1:
            if switch_status[center+cnt] == switch_status[center-cnt]:
                if switch_status[center+cnt] == 1:
                    switch_status[center + cnt], switch_status[center - cnt] = 0, 0
                else:
                    switch_status[center + cnt], switch_status[center - cnt] = 1, 1
            cnt += 1
        # print(switch_status)

if len(switch_status) > 20:
    i = len(switch_status)%20
    for j in range(i):
        for z in range(j)

else:
    print(*switch_status)


