import sys
sys.stdin = open('2805.txt')

map()

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    farms = [list(map(int, input()))for _ in range(N)]
    # print(farms)
    n = N // 2
    ups = farms[:n]
    middles = farms[n]
    downs = farms[n + 1:]
    downs = downs[::-1]
    # print(ups)
    #칸 위 아래 나누고
    #중앙은 걍 다 더하고
    # 위는 위에서 부터 n인덱스부터 1~n까지 좌우로 더한 인덱스 계산
    sums = 0
    if n == 0:
        print('#{}'.format(tc), *farms[0])
    elif n == 1:
        sums += sum(middles)
        sums += ups[0][n]
        sums += downs[0][n]
        print('#{}'.format(tc), sums)
    elif n > 1: #3
        sums += sum(middles)
        for i in range(n): #0,1,2
            sums += ups[i][n] #0 3
            sums += downs[i][n] # 03
            if i >= 1:
                for j in range(1, i+1):# 1, 2
                    sums += ups[i][n-j] #02 04 11 12 14 15   2 2
                    sums += ups[i][n+j]
                    sums += downs[i][n-j]
                    sums += downs[i][n+j]
        print('#{}'.format(tc), sums)