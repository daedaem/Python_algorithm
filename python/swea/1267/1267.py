import sys
sys.stdin = open('1267.txt')
TC = 10
for index in range(1, 11):
    V, E = map(int, input().split())
    numberlist = list(map(int, input().split()))
    # 4 1 1 2 2 3 2 7 5 6 7 6 1 5 8 5 8 9
 1 2 3 4 5 6 7 8 9
    
    # print('#{} {}'.format(index, ))