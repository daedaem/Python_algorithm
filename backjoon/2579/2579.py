import sys
sys.stdin= open('2579.txt')
N = int(input())
stairs = []
visited = [0] * (N+1)
for _ in range(N):
    x= int(input())
    stairs.append(x)
record = []
# print(x)
print(stairs)

def sumstair(x, visited):
    if while



1
1       10

2
12      30
2       20

3
1,3     25
2,3     35      

4
1,2,4   55
1,3,4   50
2,4     45

5
1   2   4   5       65
1,  3   5           35
2   3   5           45
2   4   5           55