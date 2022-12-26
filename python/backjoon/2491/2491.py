import sys
sys.stdin = open('2491.txt')

N = int(input())
num_list = list(map(int, input().split()))
print(num_list)
stack = [0]
temp = 0
# for i in range(len(num_list)-1):
#     if num_list[i] <= num_list[i+1]:
#         if stack[-1] == '<':
#             temp +1
#         stack.append('<')
#     if num_list[i] >= num_list[i+1]:
#         temp +=1
#     if num_list[i] != num_list[i+1]
for i in range(len(num_list)-1):
    if num_list[i] < num_list[i+1]:
        stack.append('<')
    if num_list[i] > num_list[i+1]:
        stack.append('>')
    if num_list[i] == num_list[i+1]:
        stack.append('=')
print(stack)
# temp = 0
# result = []
# for j in range(len(num_list)):
#     if num_list[j] == num_list[j+1] or num_list == '=':
#
#     if num_list[j] != '':0


