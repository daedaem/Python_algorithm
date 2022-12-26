import sys
sys.stdin=open('1251.txt')
char = input()
wordslist = []
result = []
for i in range(len(char)-2):
    for j in range(i+1, len(char)-1):
        temp = ''
        temp += char[:i+1][::-1]
        temp += char[i+1:j+1][::-1]
        temp += char[j+1:][::-1]
        result +=[temp]
# print(result)
result.sort()
# print(result)
print(result[0])
# for i in range(len(result)):
#     for j in range(len(char)):
#     result[i][j]
# for i in range(len(newlist)):
#     for j in range(len(char)):
#
#         newlist[i][j]
            # if newlist[j][i]
# 난중에 인덱스로 문자 구하기
#         temp += char[][]
#         temp += char[j][::-1]
#             wordslist.append(char[i]+char[j]+char[z])
