import sys
sys.stdin=open('1220.txt')
# N극 성질 1
# S극 성질 2
# N극이 윗부분
# S극이 아래
for tc in range(1, 10+1):
    N = int(input())
    tables = [list(map(int, input().split())) for _ in range(N)]
    # print(tables)
    # print(tables)
    # N극(1)인 경우, 행 +1이 2이면 교착. 행
    # S극(2)인 경우, 행 -1이 2이면 교착, 행
    cnt = 0
    for i in range(N):
        for j in range(N-1):
            if tables[j][i] == 1:
                if tables[j+1][i] == 0:
                    tables[j + 1][i] = 1
                elif tables[j + 1][i] == 2:
                    cnt+=1
            elif tables[j][i] == 2:
                if tables[j + 1][i] == 0:
                    tables[j + 1][i] = 2
    print('#{}'.format(tc), cnt)

    ##### 오답1. 행에서 0 압축
    # new_tables = [[] for _ in range(N)]
    # for i in range(N):
    #     for j in range(N):
    #         if tables[j][i] == 0:
    #             pass
    #         else:
    #             new_tables[j].append(tables[j][i])
    # # print(new_tables)
    # for i in range(len(new_tables)):
    #     for j in range(len(new_tables[i])):
    # stack = [0]

    ## 오답2. 스택쌓기
    # for i in range(N):
    #     stack =[0]
    #     for j in range(N):
    #         if tables[j][i] == 2:
    #             if stack[-1] == 1:
    #                 stack.pop(-1)
    #                 cnt += 1
    #             elif stack[-1] == 1:
    #                 stack.append(tables[j][i])
    #         elif tables[j][i] == 1:
    #             stack.append(tables[j][i])

