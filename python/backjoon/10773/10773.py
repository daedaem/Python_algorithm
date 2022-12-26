import sys
sys.stdin = open('10773.txt')

K = int(input())
stack = []
numlist = [int(input()) for _ in range(K)]
for i in numlist:
    if i != 0:
        stack.append(i)
    elif i == 0 and len(stack) >=1:
        stack.pop()
print(sum(stack))
# print(numlist)