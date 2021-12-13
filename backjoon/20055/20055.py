import sys
sys.stdin=open('20055.txt')

N, K = map(int, input().split())
# print(N,K)
total =list(map(int, input().split()))
visited = [0] * N
# cnt 는 갯수
cnt = 1
while True:
    # 1.벨트 회전
    total.insert(0, total.pop())
    # 로봇 회전
    visited.insert(0, visited.pop())
    # 로봇이 내리는 N자리 위치에 오면 빼준다 = 0으로 초기화
    visited[-1] = 0

    #2.
    for i in range(N-2, -1, -1):
        if visited[i] == 1 and visited[i+1] == 0:
            if total[i + 1] >= 1:
                total[i+1] -= 1
                visited[i+1] = 1
                visited[i] = 0
    visited[-1] = 0

    #3.# 로봇이 있는지 없는지 체크, 없다면 올리고
    if visited[0] == 0 and total[0] > 0:
        total[0] -= 1
        visited[0] = 1

    # 4
    if total.count(0) >= K:
        print(cnt)
        break
    cnt +=1
# print(cnt)








    #
    # # N까지 이동하면 내리고 total[N]까지만
    # # while cnt == 2*N-1:
    # # print(cnt)
    # # 내구도 0인 갯수
    # cnt = 0
    # # 벨트위 내구도가 0보다 크면
    # if total[0] > 0:
    #     # 벨트위에 올리고 내구도 -1 감소
    #     total[0] -= 1
    #     # 방문표시
    #     visited[0] += 1
    # # else:
    #
    # # 만약 로봇이 올려져있다면 컨베이어벨트 움직이면서 -1
    # for i in range(N):
    #     if visited[i] ==1:
    #         total[i] -=1
    # if sum(visited) == N:
    #     visited = [0] * N
    # for i in range(2*N):
    #     if total.count(0) >= K:
    #         break
    #     else:
    #         cnt = 0
    # print(cnt)

    #N번에서 내린다.
    # if visited[-1] == 1:
        # 넘기기만 한다
    # print('벨트 상태', total)
    # print('방문표시', visited)
    # print(cnt)
# print(total)
#4. 만약에 내구도 0인 칸이 k개 이상이라면 과정 종료
# if cnt >=K:
#     print(cnt)
#     break
# #2. 칸이 움직인다.
# for i in range(2*N):
#     #롯
#     upside[0] -=1
