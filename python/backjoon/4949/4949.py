import sys
sys.stdin = open('4949.txt')

tc = 8
for index in range(tc):
    wordlist = input()
    # print(wordlist)
    # 짝아니면 no 맞으면 pop
    # 다시 왼쪽 괄호면 넣고 오른쪽 괄호나올때까지 push
    # 만약에 문자열 다 순회했는데 스택의 길이가 0이 되면 yes
    # 스택의 길이가 0이아니거나 문자열에 괄호 남아있으면 no
    stack = []
    for char in wordlist:
        if len(wordlist) > 1:
            if char == '.' and len(stack) == 0:
                print('yes')
                break
            # 문자열 순회하면서 (,[ 나오면 스택에 push
            if char == '(':
                stack.append(char)
            if char == '[':
                stack.append(char)
            # 만약 오른쪽 괄호 나오면 스택에서 POP 해서 비교
            elif char == ']':
                #check_word 비교할 문자열
                if len(stack) == 0:
                    print('no')
                    break
                elif stack[-1] == '[':
                    stack.pop()
                elif stack[-1] != '[':
                    print('no')
                    break
            elif char == ')':
                #check_word 비교할 문자열
                if len(stack) == 0:
                    print('no')
                    break
                elif stack[-1] == '(':
                    stack.pop()
                elif stack[-1] != '(':
                    print('no')
                    break
            #괄호 아닌 문자열 패스
            else:
                pass
        if len(wordlist) <= 1:
            pass


        ### 1. 왼쪽 괄호 남았을 때 처리
        ### 2. 길이가 0일때 yes or no 처리