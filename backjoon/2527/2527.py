import sys
sys.stdin = open('2527.txt')
squares = [int(input().split()) for _ in range(4)]
print(squares)
# x=[int(input().split()[1])for _ in range(6)]*2