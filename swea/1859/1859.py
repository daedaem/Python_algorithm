import sys
sys.stdin = open('1859.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    number_list = list(map(int, input().split()))
    # print(number_list)
    total = 0
    # 맥스값의 전날까지  맥스값보다 작으면 사고
    # 앞인덱스부터 골라서 나머지 값중에 차이가 가장 큰거구하고
    # 만약에 음수가 나오면 안산다.
    new = [1]
    while True:
        if sum(new) == 0:
            break
        else:
            max_value = max(number_list)
            max_value_index = number_list.index(max_value)
            new = number_list[:max_value_index]
            total += max_value - sum(new)
    print(total)

    1 49 200
    199 151 350
    50 150




    # for i in range(N-1):
    #     max_value = 0
    #     for j in range(i+1, N):
    #         if number_list[j] - number_list[i] > max_value:
    #             max_value = number_list[j] - number_list[i]
    #     total += max_value
    # print('#{}'.format(tc), total)

