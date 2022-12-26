import sys
sys.stdin = open('2578.txt')
origin = [list(map(int, input().split())) for _ in range(10)]
bingolist = origin[:5]
calls = origin[5:]
#다음번에는 record 굳이 새로 만들지말고 blignolist의 그자리에 0처리해도 될듯
record = [[0] * 5 for _ in range(5)]
# print(calls)
#부른 번호들 리스트 called_number
called_number = []
for i in range(5):
    for j in range(5):
        called_number += [calls[i][j]]
# print(called_number)

# 부른 번호를 표시하고 줄이 빙고줄인지 확인
cnt = 0
result = 0
for num in called_number:
    if cnt >=3:
        print(called_number.index(result)+1)
        break
    for i in range(5):
        if num in bingolist[i]:
            f_r_index = bingolist[i].index(num)
            record[i][f_r_index] = 1
            #위까지는 뽑은 숫자를 체크하기
            cnt = 0
            sumr = 0
            suml = 0
            for c in range(5):
                sumx = 0
                sumy = 0
                sumr += record[c][c]
                suml += record[c][4-c]
                if suml == 5:
                    cnt += 1
                if sumr == 5:
                    cnt += 1
                for z in range(5):
                    sumx += record[c][z]
                    sumy += record[z][c]
                if sumx == 5:
                    cnt += 1
                if sumy == 5:# 아니면 나눠서 적어라
                    cnt+=1
                if cnt >= 3:
                    result = num
                    break
# print(called_number.index(result)+1)
            # print(record)
            # if sum(record[i]) == 5:
            #     cnt += 1
            # if sum(record[f_r_index][i]) == 5:
            #     cnt += 1

    # for j in range(5):# 시간 초과면 i로만
        #     if bingolist[i][j] == num:
        #         bingo_record[i][j] += 1
        #         # 만약 합이 5가 되면 cnt+=1
        #         if sum(bingo_record[i]) == 5:
        #             cnt +=1
        #         if sum(bingo_record[j]) == 5:
        #             cnt +=1
        #         break
        # break
        #

    # if bingo_record[]
    # print(bingo_record)
# origin = [list(map(int,input().split())) for _ in range(10)]
# bingolist = origin[:5]
# calls = origin[5:]
# # print(origin)
# print(bingolist)
# print(calls)
# bingo_record = [[0] * 5 for _ in range(5)]
# # print(bingo_record)
# #
# bingo_calledlist = []
# for i in range(5):
#     for j in range(5):
#         bingo_calledlist += [calls[i][j]] # 5 10 7 16   i0  j0~4
#         #방법1.calledlist에 담아서 다시 시작하는거
#         #방법2.그대로 이용# 어렵다
# print(bingo_calledlist)
# for i in bingo_calledlist:
#     for j in range(5):
#         for c in range(5):
#             bingolist[c].index(i)
#             bingo_record[j][c] += 1
#             print(bingo_record)
#
#
#         # bingo_record_value = calls[i][j]
#         # for z in range(5):
#         #     print(bingolist[z])
#         #     if x in bingolist[z]
#         #
#         #     break
#         # bingo_calledlist.append([i,j])
#         # record[i][j]
# #불려야할 빙고 숫자들 담기
# # print(bingo_calledlist)
# # for i in range(len(bingo_calledlist)):
# #     # for j in range(3):
# #     bingo_record[bingo_calledlist[i][0]][bingo_calledlist[i][1]] += 1
# #     for
# #     if bingo_record[i][i]
#
#
# cnt =0
# # for i in range(len(bingo_calledlist)):
# #     if i in
#
# #### 이제부터는 하나씩 꺼내서 나온 숫자들을 만든 빙고판에 하나씩 1추가
# # 만약 가로 세로 좌하방 대각 우하방대각이 모두 같은 숫자일때
# # cnt+1 하고 cnt가 일때, bingo_calledlist의 인덱스 출력
#
#
#
# #         print(temp.index(bingo_record_index))
#
# # for c in range(5):
# #             for z in range(5):
# #             print(bingolist[c][z].index(bingo_record_index))
# # # print(bingo_record)