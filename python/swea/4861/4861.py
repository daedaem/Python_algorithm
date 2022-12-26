import sys
sys.stdin = open('4861.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    words = [input() for i in range(N)]
    # print(N)
    print(words)
    result = ''
    print(list(zip(range(3), range(4))))
    for i in zip(*words):
        


    # A = list(zip(words[0]))
    # for i in range(len(A)):
    #     result += str(A[i])
    # print(result)
    # 가로부터
    # result = []
    # for i in range(N):
    #     for j in range(N-M+1): # 체크
    #         temp = []
    #         cnt = 0
    #         for c in range(M):
    #             temp+= words[i][j+c]
    #         if temp == temp[::-1]:
    #             result.append(temp)
    #
    #             # print(temp)
    #         # for z in range(M//2): #4(2), 6(3)
    # #             if temp[z] == temp[-(z+1)]:
    # #                 cnt +=1
    # #         if M%2:
    # #             if cnt == len(temp)//2+1:
    # #                 result.append(temp)
    # #             else:
    # #                 break
    # #         else:
    # #             if cnt == len(temp)//2:
    # #                 result.append(temp)
    # #             else:
    # #                 break
    # # # print(result)
    # # 세로
    # for i in range(N):
    #     for j in range(N-M+1): # 체크
    #         temp = []
    #         cnt = 0
    #         for c in range(M):
    #             temp+= words[j+c][i]
    #         # print(temp)
    #         if temp == temp[::-1]:
    #             result.append(temp)
    #         # for z in range(M//2): #4(2), 6(3)
    #         #     if temp[z] == temp[-(z+1)]:
    #         #         cnt +=1
    #         # if M%2:
    #         #     if cnt == len(temp)//2+1:
    #         #         result.append(temp)
    #         #
    #         # else:
    #         #     if cnt == len(temp)//2:
    #         #         result.append(temp)
    #         #     else:
    #         #         break
    # # print(result)
    # cnt = ''
    # for i in result:
    #     for j in i:
    #         cnt +=j
    # print('#{}'.format(tc), cnt)

        # print(result[i])
    # print(result)