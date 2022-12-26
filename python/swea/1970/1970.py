import sys
sys.stdin=open('1970.txt')

T = int(input())
korea_current_list = [10, 50, 100, 500, 1000, 5000, 10000, 50000][::-1]
# print(korea_current_list)
for t in range(1, T+1):
    current_count = [0] * 8
    N = int(input())
    # print(N)
    temp = N
    for i in range(8):
        current_count[i] += temp // korea_current_list[i]
        temp = temp % korea_current_list[i]
    print('#{}'.format(t))
    print(*current_count)
