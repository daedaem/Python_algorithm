import sys
sys.stdin = open('1158.txt')

N, K = map(int, input().split())
# print(N)
orders = 0
stack = []
members = list(range(1,N+1))
# print(members)
while members:
    orders += K-1
    if orders >= len(members):
        while orders >= len(members):
            orders -=len(members)
            # print(orders)
            # print(members)
        x = members.pop(orders)
        stack.append(x)
    else:
        x = members.pop(orders)
        stack.append(x)
        # print(members)
        # print(orders)
# print(*stack)

print('<', end="")
for i in range(len(stack)-1):
    print(stack[i], end=", ")
print(stack[-1], end=">")
