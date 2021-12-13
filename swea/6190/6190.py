import sys
sys.stdin=open('6190.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numb_list = list(map(int, input().split()))
    # print(N)
    for i in range(N-1):
        for j in range(i+1, N):
            if numb_list[i] = numb_list[i+1]:
                numb_list[i], numb_list[i + 1] = numb_list[i + 1], numb_list[i]

    # numb_list.sort()
    # print(numb_list)
    result = []
    for i in range(N-1):
        for j in range(i+1, N):
            temp = list(str(numb_list[i] * numb_list[j]))
            print(temp)
            max_char = int(temp[0])
            chars = str(temp[0])
            if len(temp) == 1:
                result.append(int(temp[0]))
            elif len(temp) > 1:
                for z in range(1, len(temp)):
                    print(int(temp[z]))
                    if int(temp[0]) <= int(temp[z]):
                        chars += temp[z]
            result +=[chars]
    if len(result) == 0:
        print('#{}'.format(tc), -1)
    else:
        max_result =int(result[0])
        for i in range(len(result)):
            if max_result <= int(result[i]):
                max_result = int(result[i])
        print('#{}'.format(tc), max_result)