import sys
sys.stdin = open('2001.txt')

t = int(input())
for index in range(1, t+1):
    N, M = list(map(int, input().split()))
    maze = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum = 0
            for z in range(0, M):
                for c in range(0, M):
                    sum += maze[i+z][j+c]
                    if result < sum:
                        result = sum
    print('#{} {}'.format(index, result))
