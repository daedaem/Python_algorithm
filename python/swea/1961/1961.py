import sys
sys.stdin = open('1961.txt')

t = int(input())
for tc in range(1, t+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    # 90

    record_90 = [[0]*N for _ in range(N)]
    for i in range(N): # 0, 1, 2
        for j in range(N): # 0, 1, 2
            record_90[j][N-1-i] = str(arr[i][j])


    record_180 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            record_180[N-i-1][N-j-1]= str(arr[i][j])



    record_270 = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            record_270[N-j-1][i] = str(arr[i][j])

    # print(record_90)
    new_90=[]
    new_180=[]
    new_270=[]
    temp =''
    for i in range(N):
        temp = ''
        for j in range(N):
            temp += record_90[i][j]
        new_90.append(temp)

    for i in range(N):
        temp = ''
        for j in range(N):
            temp += record_180[i][j]
        new_180.append(temp)

    for i in range(N):
        temp = ''
        for j in range(N):
            temp += record_270[i][j]
        new_270.append(temp)

    print('#{}'.format(tc))
    for i in range(N):
        print(new_90[i], end=' ')
        print(new_180[i], end=' ')
        print(new_270[i], end=' ')
        print()



