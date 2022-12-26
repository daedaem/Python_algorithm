import sys
sys.stdin=open('2491.txt')

N = int(input())
num_list = list(map(int, input().split()))
# print(num_list)
# cnt_1 = 1
# cnt_2 = 1
# cnt_result = []
#
# for i in range(N-1):
#     if num_list[i] <= num_list[i+1]:
#         cnt_1 += 1
#         cnt_result.append(cnt_1)
#     else:
#         cnt_1 = 1
# for j in range(N-1):
#     if num_list[j] >= num_list[j+1]:
#         cnt_2 += 1
#         cnt_result.append(cnt_2)
#     else:
#         cnt_2 = 1
result = []
cnt1 = 1
cnt2 = 1
for i in range(N-1):
    for j in range(i+1, N):
        if num_list[j-1] <= num_list[j]:
            cnt1 += 1
        else:
            result.append(cnt1)
            cnt1 = 1
            break
for i in range(N-1):
    for j in range(i+1, N):
        if num_list[j-1] <= num_list[j]:
            cnt2 += 1
        else:
            result.append(cnt2)
            cnt2 = 1
            break
print(result)


# print(cnt_result1)
# print(cnt_result2)
# print(max(cnt_result))


# 젤 긴 길이 출력, 길이가 3 미만인 경우 2출력
# result = []
# record = [0]*(N+1)
# stack = []
# for i in range(N-1):
#     if i == 0:
#         if num_list[0] < num_list[1]:
#             stack.append('<')
#         elif num_list[0] > num_list[1]:
#             stack.append('>')
#         elif num_list[0] == num_list[1]:
#             stack.append('=')
#     else: # 스택 없을 때 스택 초기화
#         if num_list[i] < num_list[i+1]:
#            x = stack.pop()
#            if x =='>':
#                result.append('<')
#            elif x =='<':
#                stack.append('<')
#                result.append('<')
#            elif x == '=':
#                stack.append('=')
#                result.append('<')
#         elif num_list[i] > num_list[i + 1]:
#             x = stack.pop()
#             if x == '<':
#                 result.append('<')
#             elif x == '>':
#                 stack.append('>')
#                 result.append('>')
#             elif x == '=':
#                 stack.append('=')
#                 result.append('>')
#         elif num_list[i] == num_list[i+1]:
#             x = stack.pop()
#             if x == '=':
#                 result.append('=')
#             elif x == '<':
#                 stack.append('=')
#                 result.append('<')
#             elif x == '>':
#                 stack.append('=')
#                 result.append('<')
