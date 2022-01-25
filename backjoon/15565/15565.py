import sys
from collections import deque
que= deque()
sys.stdin=open('15565.txt')

N, K = map(int, input().split())
doll_info = list(map(int, input().split()))
group_count = N

# doll_value = K
start = 0
end=0
temp = 0

if K==N:
    print(K)
else:
    if doll_info.count(1) < K:
        print(-1)
    else:
        # 맨 처음 1 연속된 집합 찾기
        for i in range(N):
            if doll_info[i]==1:
                temp +=1
                que.append(i)
            if temp == K:
                initial_group_count = i+1
                break
        que.popleft()
        # print(que)
        while len(que)>1:
            start = que.popleft()
            end = que.popleft()
            value_temp = 2
            len_temp=0
            if end+1 > N:
                break
            else:
                for i in range(end+1, N):
                    if doll_info[i] == 1:
                        value_temp += 1
                        if value_temp == K:
                            len_temp = i-start+1
                        if initial_group_count> len_temp:
                            initial_group_count=len_temp
                            start = end
                            end = i
                            que.append(start)
                            que.append(end)
                            break
        print(initial_group_count)




        # while doll_info:
        # 처음에 1위치 찾고
        # print(doll_info.index(1))





        # while doll_info:
        #     temp = 0
        #     for i in range(start, N):
        #         if doll_info[start] == 2:
        #             break
        #         if i-start+1 > group_count:
        #             break
        #         if doll_info[i] == 1:
        #             temp += 1
        #         if temp == K:
        #             if group_count > i-start+1:
        #                 group_count = i-start+1
        #             else:
        #                 pass
        #             break
        #         # if temp < K and start == 0:
        #         #     print(-1)
        #         #     break
        #     start+=1
        #     if start==N:
        #         break
        # print(group_count)



# doll_info[start]

