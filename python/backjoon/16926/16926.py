import sys
sys.stdin=open('16926.txt')

N,M,R = map(int,input().split())

numlist = [list(map(int,input().split())) for _ in range(N)]
print(numlist)