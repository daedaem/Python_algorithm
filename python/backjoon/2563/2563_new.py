import sys
sys.stdin = open('2563.txt')

total=int(input())
square_len=10
square_list = [list(map(int, input().split())) for _ in range(total)]
records = [[0]*100 for _ in range(100)]
# print(records)
# print(square_list)
x=[]
y=[]
for i in range(total):
    x.append([square_list[i][0], square_list[i][0]+10])
    y.append([square_list[i][1], square_list[i][1]+10])
# print(x)
# print(y)
for i in range(total):
    for j in range(y[i][0], y[i][1]):
        for z in range(x[i][0], x[i][1]):
            if records[j][z] == 1:
                pass
            else:
                records[j][z] +=1
# print(records)
sums =0
for i in range(len(records)):
    sums += sum(records[i])
print(sums)

