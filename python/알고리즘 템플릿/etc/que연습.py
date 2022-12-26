from collections import deque

arr = deque()
acc = deque()
arr.append(1)
arr.append(2)
acc.append(4)
# print(arr)
arr.reverse()
print(arr)
print(acc)
arr.popleft()
print(arr)
print(acc)
# print(arr.__len__())
# for i in arr:
#     print(i)