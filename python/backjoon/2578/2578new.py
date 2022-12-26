import sys
sys.stdin=open('2578.txt')
# 5X5줄 빙고 선 3개
binggo = [list(map(int, input().split())) for _ in range(5)]
# print(binggo)
# print('-' * 50)
calling = [list(map(int, input().split())) for _ in range(5)]
# calling = [input().split() for _ in range(5)]
# print(calling)
# print(calling)
record = [[0] * 5 for _ in range(5)]
# print(record)
# print(calling)
for i in range(5):
    for j in range(5):
        for z in range(5):
            if calling[i][j] in binggo[z]:
                v = binggo[z].index(calling[i][j])
                record[z][v] = 1
                # if record[]
            else:
                pass


        # 콜링 숫자를 binggo에서 찾고 record의 각각 레코드에 기록
        # binggo[i].index()

