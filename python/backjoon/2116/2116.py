import sys
sys.stdin = open('2116.txt')
n =int(input())
diceinfo = [list(map(int, input().split())) for _ in range(n)]

newdice = []
for i in range(n):
    temp = []
    temp.append([diceinfo[i][0], diceinfo[i][5]])
    temp.append([diceinfo[i][1], diceinfo[i][3]])
    temp.append([diceinfo[i][2], diceinfo[i][4]])
    newdice += [temp]
sum_result = 0
stack = []
for z in range(1, 7):
    sums = 0
    for i in range(n):
        for j in range(3):
           if z in newdice[i][j]:
               y = newdice[i][j].index(z)
               if y == 1:
                   z = newdice[i][j][0]
               else:
                   z = newdice[i][j][1]
               mome = newdice[i].pop(j)
               sums += max(max(newdice[i][0]), max(newdice[i][1]))
               newdice[i].insert(j, mome)
               break
    stack.append(sums)
    sum_result = max(stack)
print(sum_result)