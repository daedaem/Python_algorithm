import sys
sys.stdin=open('1974.txt')

t = int(input())
for tc in range(1, t+1):
    puzzle = [list(map(int, input().split())) for _ in range(9)]
    # print(puzzle)
    # print(sum(range(1, 10)))
    yes = []
    no =[]
    #가로확인
    for i in range(9):
        if sum(puzzle[i]) == 45:
            yes +=[1]
        elif sum(puzzle[i])!=45:
            no +=[1]
    #세로확인
    tempyes=0
    tempno=0
    for i in range(9):
        tempyes = 0
        for j in range(9):
            tempyes += puzzle[j][i]
        if tempyes == 45:
            yes += [1]
        else:
            no +=[1]

    #박스안 확인
    temp=0
    for i in range(0, 7, 3):
        for x in range(0, 7, 3):
        # print(i)
            temp = 0
            for j in range(3):
                for z in range(3):
                    temp += puzzle[i+j][x+z]
            if temp == 45:
                yes += [1]
            else:
                no += [1]

    if len(no) == 0:
        print('#{}'.format(tc), 1)
    else:
        print('#{}'.format(tc), 0)
        #     tempyes += puzzle[j][i]
        # if tempyes == 45:
        #     yes += [1]
        # else:
        #     no +=[1]


    #
    #         elif sum(puzzle[i]) != 45:
    #             no += [1]
    #
    #         # if sum(puzzle[j][i])==45:
    #         #     yes += [1]
    #         # elif sum(puzzle[j][i])!=45:
    #         #     no +=[1]
    #
    # print(no)
