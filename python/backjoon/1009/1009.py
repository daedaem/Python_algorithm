import sys
sys.stdin=open('1009.txt')

T = int(input())

for tc in range(1, T+1):
    a,b = map(int,input().split())
    if a% 10 ==0:
        print(10)
    elif a %10 ==1:
        print(1)
    elif a %10 ==2:
        if b%4 ==0:
            print(6)
        elif b%4 ==1:
            print(2)
        elif b%4 ==2:
            print(4)
        else:
            print(8)
    elif a %10==3:
        if b%4 ==0:
            print(1)
        elif b%4 ==1:
            print(3)
        elif b%4 ==2:
            print(9)
        else:
            print(7)
    elif a %10==4:
        if b%2 ==0:
            print(6)
        elif b%2 ==1:
            print(4)
    elif a %10==5:
        print(5)
    elif a %10==6:
        print(6)
    elif a %10==7:
        if b%4 ==0:
            print(1)
        elif b%4 ==1:
            print(7)
        elif b % 4 == 2:
            print(9)
        else:
            print(3)
    elif a %10==8:
        if b % 4 == 0:
            print(6)
        elif b % 4 == 1:
            print(8)
        elif b % 4 == 2:
            print(4)
        elif b % 4 == 3:
            print(2)
    elif a %10==9:
        if b % 2 == 0:
            print(1)
        elif b % 2 == 1:
            print(9)