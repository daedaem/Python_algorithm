import sys
sys.stdin=open('2615.txt')
# index+4까지 가로. 세로, 대각선 체크 1,2

badook = [list(map(int, input().split())) for _ in range(19)]
# print(badook)
badooks = badook
# for i in range(19):
#     badooks.append(list(badook[i]))
# print(badooks)
result = []
tempw = []
temph = []
tempc1=[]
tempc2=[]
for i in range(19):
    for j in range(19):
        for z in range(5):# i!=13 or j!=13 and ! = i나 j+6
            # 5개가 같은경우 1. i+z<19 and 6개까지 같은 경우는 패스
            # 범위가 바둑판안에서
            if 0 <= i+z <= 18 and 0<= j+z <= 18 and badooks[i][j] != 0 :
                temph += [badooks[i+z][j]]
                tempw += [badooks[i ][j+z]]
                tempc1 += [badooks[i + z][j+z]]
                tempc2 += [badooks[i - z][j-z]]

                # if  i+z < or j+z and badooks[i][j] * 6 == sum(temp):
                #     pass
                # else:
        # print(temph)
        # print(tempw)
        # print(tempc1)
        # print(tempc2)
        if badooks[i][j] * 5 == sum(tempw):
            result.append(tempw)
        if badooks[i][j] * 5 == sum(temph):
            result.append(temph)
        if badooks[i][j] * 5 == sum(tempc1):
            result.append(tempc1)
        if badooks[i][j] * 5 == sum(tempc2):
            result.append(tempc2)
print(result)
                # if  i+z < or j+z and badooks[i][j] * 6 == sum(temp):
                #     pass
                # else:





        # print(badooks[i][j])
        # 0이 아니고 그자리에서 +4까지
        # 상좌우하, 우상좌하
#         if badooks[i][j] != 0:
#             if badooks[i][j] == badooks[i][j + 1] == badooks[i][j+2] == badooks[i][j+3] == badooks[i][j+4] != badooks[i][j+5] or badooks[i][j] == badooks[i+1][j] == badooks[i+2][j] == badooks[i+3][j] == badooks[i+4][j] != badooks[i+5][j] or badooks[i][j] == badooks[i + 1][j+1] == badooks[i + 2][j+2] == badooks[i + 3][j+3] == badooks[i + 4][j+4] != badooks[i+5][j+5] or badooks[i][j] == badooks[i + 1][j+1] == badooks[i + 2][j+2] == badooks[i + 3][j+3] == badooks[i + 4][j+4] != badooks[i+5][j+5]:
#                 result += badooks[i][j], i+1, j+1
#         else:
#             pass
# # print(result)
# if len(result) > 1:
#     print(result[0])
#     print(result[1], result[2])
# else:
#     print(0)
#
