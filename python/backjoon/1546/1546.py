import sys
sys.stdin = open('1546.txt')
N = int(input())

scores = list(map(int,input().split()))
# print(scores)
result = sum(scores)/ max(scores)*100 / N
print(result)