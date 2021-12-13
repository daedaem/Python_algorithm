import sys
sys.stdin = open('1874.txt')
n = int(input())
numlist = list(range(1, n+1))
x = list(map(int, input()) for _ in range(n))
pro = []
stack = []
# print(numlist)
# print(x)
# 숫자 1~n까지 리스트를 하나씩 꺼내서 stack에 push. 출력과정리스트 +  추가
# 입력받은 값을 순회 i값과 비교하고 같으면 stack에서 pop. 출력과정리스트 -추가
# 같으면 비교할 리스트에 push 숫자리스트에서 pop

#1234에서 앞에서부터 하나씩 팝해서 sta
for i in range(n):
    for j in numlist:
        if len(stack) != 0 and stack[-1] == x[i]:
            stack.pop()
            pro.append('-')
            break
        elif x[i] != j:
            numlist.pop(0)
            stack.append(j)
            pro.append('+')
        elif x[i] == j:
            numlist.pop(0)
            stack.append(j)
            pro.append('+')
            stack.pop()
            pro.append('-')
            break
    print(pro)
# 최종적으로 입력값과 내가 만든 수열값이 같은지 확인