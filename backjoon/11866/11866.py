import sys
sys.stdin = open("11866.txt")
n, k = map(int, input().split())
# print(n, k)
stack=[]
arrs = list(range(1, n+1))
k = k-1
indexs = k
# print(arrs)
while len(arrs) != 0:
    if len(arrs) <= k:
        k = k % len(arrs)
        y = arrs.pop(k)
        stack.append(y)
        k += indexs
    if len(arrs) > k:
        y = arrs.pop(k)
        stack.append(y)
        k += indexs
result = []
for i in stack:
    if len(stack)>1:
        if i == stack[0]:
            y = '<' + str(i)+','
        elif i == stack[-1]:
            y = str(i) + '>'
        else:
            y = str(i)+','
        result.append(y)
    else:
        print('<{}>'.format(*stack))
print(*result)

# ck:
#     print('<i')

# 1234567  길이7 인덱스2  값3
# 124567 길이6 인덱스4 값6
# 12457 길이5 인덱스6(=1) 값2
# 1457 길이4 인덱스 3 값 7
# 145 (5-3 = 2) 5
# 14 (0)


# # print(n, k)
# x = list(range(1, n+1))
# que = []
# # print(x)
# while k > 0:
#     if len(x) > k:
#         que.append(x.pop(k-1))
#         k += k-1
#     if k > len(x):
#         k = k % len(x)
#         que.append(x.pop(k-1))
#         k += k-1
#     if len(x) == 0:
#         print(*que)
#         break
# #   if 0 < len(x) < k:
# #         que.append(x.pop(k))
#         k -= len(x)+1
#     if len(x) > k:
#         que.append(x.pop(k))
#         k += k
#     if len(que) == n:
#         print(*que)
#         break

# print(n,k)
# x = list(range(1, n+1))* K
# # print(x)
# result = []
# while k > 0 :
#     result.append(x[k])
#     k+=k
#     print(k)
#     if len(result) == n:
#         print(*result)
#         break