import sys
sys.stdin = open('17413.txt')

data = input()
# print(len(data))
temp = ''
result = []
stack = ''
pos = 0

while pos < len(data):
    if data[pos] == '<':
        result.append(temp[::-1])
        temp =''
        while data[pos] !='>':
            stack += data[pos]
            pos +=1
    elif data[pos] =='>':
        stack += data[pos]
        result.append(stack)
        stack =''
        pos +=1
    elif data[pos] == ' ':
        result.append(temp[::-1])
        result.append(data[pos])
        temp =''
        pos += 1
    else:
        temp += data[pos]
        pos += 1
if pos == len(data) and temp !='':
    result.append(temp[::-1])

real = ''
if result[0]=='':
    for i in result[1:]:
        real += i
    print(real)
else:
    for i in result:
        print(i, end="")

