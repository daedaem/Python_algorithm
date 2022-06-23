import sys
sys.stdin=open('3040.txt')

smallList = [int(input()) for _ in range(9)]
# print(smallList)
for i in range(len(smallList)):
    for j in range(i+1, len(smallList)):
        if sum(smallList) - (smallList[i] + smallList[j])==100:
            smallList[i] , smallList[j] =0 ,0
for i in smallList:
    if i !=0:
        print(i)

# for i in range()