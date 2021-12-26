import sys
sys.stdin = open('2078.txt')

A, B = map(int, input().split())
print(A, B)
cnt = -1
lefts = 0
rights = 0
# left_result = []
# right_result = []
result = []
stack = []

def tree(cnt, x,y):
    if x > A and y > B:
        return
    else:
        left(cnt, x,y)
        right(cnt, x,y)

def left(cnt, x,y):
    if x == A and y == B:
        return result.cnt
    elif x > A or y > B:
        return
    else:
        x += y
        tree(cnt+1, x, y)

def right(cnt, x, y):
    if x == A and y == B:
        return result.cnt
    elif x > A or y > B:
        return
    else:
        y += x
        tree(cnt+1, x, y)

print(tree(1,1))
# print(result)
