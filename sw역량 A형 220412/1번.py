import sys
sys.stdin = open("1.txt")
T= int(input())
W, H = map(int, input().split())
#w가 짝수면 밑 홀수면 위
#사이드 부분은 기존과 다르게
# 홀수 경우 맨 아래 좌우, 대각선 위 좌우
maze = list(list(map(int, input().split())) for _ in range(H))
# print(maze)

# y= [-1, -1, 0, 1, 1, 1, 0]
# X = [0, 1, 1, 1, 0, -1, -1, -1, 0]

1 2 7           2
2 1 3 7 8 9     5
3 2 4 9         3
4 3 5 9 10 11    5
5 4 6 11          2
6 5 11 12        3

7 1 2 8 13    4
8 2 7 9 13 14 15 6

7 2 6 8 11 12 13    6
8 2 3 4 7 9 13      6
9 4 8 10 13 14 15   6
10 4 5 9 15         4