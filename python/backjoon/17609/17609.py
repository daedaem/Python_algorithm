import sys
sys.stdin=open('17609.txt')

#
T = int(input())
for i in range(T):
    words = input()
    print(words)
    idx = len(words)//2
    # print(idx)
    sums=[]
    for i in range(idx):
        if words[i]== words[-i-1]:
            sums.append(0)
        else:
            sums.append(2)
    result = sum(sums)
    if result == 0:
        print(0)



    else:
        # 하나씩 빼서 위에 조건그대로
        newlist =[]
        for i in range(len(words)):




    #     words[] == words[i+1]