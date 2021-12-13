import sys
sys.stdin=open('5432.txt')

T = int(input())
for tc in range(1, T+1):
    pipe = input()
    pip_list = list(pipe)
    # print(pipe)
    stack = []
    cnt = 0
    temp = 0
    record = [[1] for _ in range(len(pip_list))]
    print(record)
    # for i in range(len(pip_list)-1):

    # for i in range(len(pip_list)-1):
    #     if pip_list[i] == '(' and pip_list[i+1] ==')':
    #         pip_list[i][i+1] = 0, 0
    # for i in range(len(pip_list)-1):
    #     if pip_list[i] =='(':
    #         stack.append('(')
    #     elif pip_list == 0:
    #         stack.append(0)
    #         if pip_list[i+1] == ')':
    #             cnt = 0
    #             while True:
    #                 cnt += 1
    #                 x = pip_list.pop()
        # elif pip_list[i] ==')':
        #     stack.append(')')



    print(pip_list)