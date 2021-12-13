import sys
sys.stdin = open('10709.txt')

H, W = map(int, input().split())
# print(H,W)
c_info = [list(input()) for _ in range(H)]
records = [[-1]* W for _ in range(H)]
# print(records)
# print(c_info)
for i in range(H):# 0 1 2
    for j in range(W-1, -1, -1): # 3 2 1 0
        # 각 줄에 c가 없으면  -1
        if 'c' not in c_info[i]:
            pass
        else: # 줄에 c가 있으면
            # 그 자리에 c가 있으면 0
            if c_info[i][j] == 'c':
                records[i][j] = 0
                # c가 없으면
            elif c_info[i][j] != 'c': #
                # j 번 왼쪽 최근 값 b
                # 밑 인덱스 j까지 인건 j왼쪽부분까지만 찾도록
                for b in range(j):
                    if c_info[i][b] == 'c': # 4  3210  0
                        records[i][j] = j-b
# 출력 형식에 맞춰서 출력하기
for i in range(len(records)):
    for j in range(W):
        print(records[i][j], end=' ')
    print()





# 오른쪽부터 시작해서 자기 자신으로부터 맨 최근 앞에 c가 있는지 체크
# 만약 그줄에 c가 없으면 -1. 자기자리에 c가 있으면 0출력

