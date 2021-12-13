import sys
sys.stdin = open('2563.txt')
totalsquare = 100*100
t = int(input())
infos = [list(map(int, (input().split()))) for _ in range(t)]
print(infos)
# 각 사각형의 끝 좌표 추가해주기
for i in range(t):
    for j in range(2):
        infos[i].append(infos[i][j]+10)
print(infos)

1-1첫번째 색종이 영역
# (3,7) 13, 17
# (15, 7) (25,17)
# (5,2) (15,12)

# 1-2두번째 색종이 영역
# 1-3세번째 색종이 영역
# 1-4. 겹치는 부분
세조건을 모두 비교하는 방법 모르겠네
x[1,2,3]
for i in range(1, t): # 1, 2' t=3
    for j in range(t-i, -1): # 2, 1, 0    1 ,2

# 겹칠때 조건
# 첫째, 1사각형 x1 < 2사각형 x1 < 1사각형 x 2
# 둘째, 1사각형 x1 < 2사각형 x2 < 1사각형 x2


#.2풀이 검은 영역에서 흰 영역 빼자
# 17x25 - 2
# 첫번째 색종이 영역
# 두번째 색종이 영역
# 세번째 색종이 영역