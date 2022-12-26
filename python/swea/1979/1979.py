import sys
sys.stdin = open('1979.txt')
t = int(input())
for tc in range(1, t+1):
    N, K = map(int, input().split())
    # print(N,K)
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    # print(puzzle)
    # 좌우 상하 한칸씩 더 비교해봐야하니까 동서남북 1칸씩추가로 벽을 만들어 준다.
    record = [[0]* (N+2) for _ in range(N+2)]
    # print(record)
    for i in range(N):
        for j in range(N):
            if puzzle[i][j] == 1:
                record[i+1][j+1] = 1
    # print(record)
    result = 0
    temp = 0
    #가로
    for i in range(N+2):
        for j in range(1, N+2-K):
            #비어있는 칸이 K개 만큼인지  temp에 1을 더해서 k가 나오는지 확인
            temp = 0
            for z in range(K):
                if record[i][j-1] == 0 and record[i][j+K] == 0:
                    temp += record[i][j+z]
                elif record[i][j-1] == 1 or record[i][j+K] == 1:
                    pass
            if temp == K:
                result += 1

    temp = 0
    #세로
    for i in range(N+2):
        for j in range(1, N+2-K):
            #비어있는 칸이 K개 만큼인지  temp에 1을 더해서 k가 나오는지 확인
            temp = 0
            for z in range(K):
                if record[j-1][i] == 0 and record[j+K][i] == 0:
                    temp += record[j+z][i]
                elif record[j - 1][i] == 0 or record[j + K][i] == 1:
                    pass
            if temp == K:
                result += 1
    print('#{}'.format(tc), result)