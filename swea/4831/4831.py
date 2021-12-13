import sys
sys.stdin=open('4831.txt')

T = int(input())
for index in range(1, T+1):
    K, N, M = map(int, input().split())
    # print(K,N,M)
    charge_list = list(map(int, input().split()))
    # print(charge_list)
    stations = [0] * (N+1)
    for i in range(M):
        stations[charge_list[i]] += K
    # print(stations)
    cnt = 0
    now = K
    energy = K

    while now < N:
        if stations[now] == K:
            cnt += 1
            now += K
            energy = K
    #         if now >= N:
    #             break
    #             # print(now)
        elif stations[now] != K:
            now -= 1
            energy -= 1
            if energy <= 0:
                cnt = 0
                break

    #         # print(now)
    print('#{} {}'.format(index, cnt))

    #
#
# for i in range(len()):
#     print(bus_list[i])
