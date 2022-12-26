import sys
sys.stdin=open('17614.txt')

N=int(input())
numlist = list(map(str, range(1,N+1)))
result = 0
for i in numlist:
    # print(i)
    result += i.count('3')+i.count('6')+i.count('9')
print(result)
#     for j in i:
#         if j=='3' or j=='6' or j=='9':
#             result+=1
# print(result)


# print(list('3'))