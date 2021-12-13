import sys
sys.stdin=open('strings.txt')
s = input()
temp = ''
result=[]
print(s)
for i in range(len(s)):
    # print(s[i])
    # 몇개씩 자를 건지
    for j in range(i):
        temp += s[j]
        temp += s[i]
        print([s[i]])
        print([s[j]])
        print([temp])
    result += temp
    temp = ''
print(result)
# temp +=



        # 자른 만큼 길이 후 인덱스
