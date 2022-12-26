import sys
sys.stdin=open("1284.txt")

while True:
    word = input()
    if word == '0':
        break
    else:
        temp =0
        for i in word:
            if int(i)==1:
                temp += 2
            elif int(i)==0:
                temp +=4
            else:
                temp+= 3
        # print(len(word))
        print(temp + len(word)+1)
#
# lines = sys.stdin.readlines()
# for line in lines:
#     # word = int(line.split())
#     # print(word)
#     # line.split('\n')
#     # print(line)
#     temp = 0
#     for i in line.split():
#         if int(i)==1:
#             temp += 2
#         elif int(i)==0:
#             temp +=4
#         else:
#             temp+= 3
#     # print(len(line))
#     print(temp + len(line)+1)

# print(lines)