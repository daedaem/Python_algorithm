import sys
sys.stdin=open('2001.txt')
t=int(input())
for index in range(1, t+1):
    N,M = map(int, input().split())
    # print(N,M)
    fly=[list(map(int, input().split())) for _ in range(N)]
    # print(fly)
    temp=0
    max_value=0
    for i in range(N-M+1):
        for j in range(N-M+1):
            temp = 0
            for z in range(M):
                for c in range(M):
                    temp += fly[i+z][j+c]
            if max_value < temp:
                max_value = temp
    print('#{}'.format(index), max_value)
