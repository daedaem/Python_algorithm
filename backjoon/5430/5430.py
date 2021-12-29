import sys
from collections import deque
sys.stdin=open('5430.txt')

def R(arr):
    if arr.__len__() <= 0:
        return
    else:
        global new_arr
        new_arr = arr.reverse()
        return new_arr

def D(arr):
    if arr.__len__() <= 0:
        return
    else:
        arr.popleft()
        if arr.__len__() == 0:
            return
        else:
            return arr

T = int(input())
for index in range(1, T+1):
    P = deque(input())
    N = int(input())
    temp = deque(input())
    temp.popleft()
    temp.pop()
    arr = deque()
    new_arr = deque()


    for i in range(P.__len__()-1):
        if P[i] == 'R' and P[i+1] == 'R':
            P[i], P[i+1] = '', ''
        else:
            pass
    # P를 다 바꿔놓고 하지말고 바꾸면서 돌려보자

    tempnumber = ''

    while temp:
        if temp[0] == ',':
            temp.popleft()
            arr.append(int(tempnumber))
            tempnumber = ''
        if temp.__len__() == 1:
            arr.append(int(temp[0]))
        if temp[0].isdigit():
            x = temp.popleft()
            tempnumber += x
    # print(arr)
    while P:
        words = P.popleft()
        if words == '':
            continue
        if words == 'R':
            R(arr)
            if arr.__len__() == 0:
                break
        if words == 'D':
            new_arr = D(arr)
            if new_arr == None:
                break
            else:
                arr = new_arr
    # if arr.__len__() == 0:
    #     # print('error')

    else:
        print(list(arr))
