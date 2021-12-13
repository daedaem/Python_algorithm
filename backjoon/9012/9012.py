import sys
sys.stdin = open('9012.txt')

# 테스트 수 받기
T = int(input())
# 수만큼 데이터 받기
for i in range(T):
    x = input()
    stack = []
    # stackgiho = []
    for i in x:
        # print(i)
        # print(i, end ='')
        if i == ')':
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
            # if len(stack) <= 0:
            #     print('NO')
            # else:
            #     stack.pop()
        else:
            stack.append(i)
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')