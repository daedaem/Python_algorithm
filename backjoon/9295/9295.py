import sys
sys.stdin=open('9295.txt')

T = int(input())
for tc in range(1, T+1):
    a,b = map(int, input().split())
    print("Case",str(tc)+":", a+b)