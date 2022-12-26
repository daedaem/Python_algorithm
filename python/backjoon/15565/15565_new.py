import sys
sys.stdin=open('15565.txt')

N, K = map(int, input().split())
doll_info = list(map(int, input().split()))
group_count = N
start=doll_info.index(1)
# print(start)
end=0

# if K==N:
#     print(K)
# else:
if doll_info.count(1) < K:
    print(-1)
else:
    while doll_info:
        temp = 0
        for i in range(start, end+1):
            if doll_info[i] == 1:
                temp += 1
            else:
                pass
        if temp == K:
            if group_count >= i-start+1:
                group_count = i-start+1
            start+=1
        if temp < K:
            end+=1
        if temp> K:
            start+=1
        if end >= N or start >= N:
            break
        # start나 end가 2가 아닐때까지 옮김
        if doll_info[start] == 2:
            while doll_info[start] == 2:
                start+=1
        if doll_info[end] == 2:
            while doll_info[end] == 2:
                end+=1
        start+=1
        end+=1
    print(group_count)


