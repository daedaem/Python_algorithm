import sys
sys.stdin=open('1032.txt')
N = int(input())
result = ''
# 한개일때는 그대로 출력
if N ==1:
    wordlist = input()
    print(wordlist)
# 한개 이상일 때는 행으로 해당 열의 문자를 하나씩 비교해서
# 같으면 result에 넣고 다르면 ?넣기
else:
    wordlist = [list(input()) for _ in range(N)]
    for j in range(len(wordlist[0])):
        # print(j)
        tempCount=0
        tempWord =''
        for i in range(N-1):
            # 같으면 tempword에 넣어서 result에 플러스
            # 다르면 break하고 ?를 넣기
            # print(wordlist[i])
            if wordlist[i][j] == wordlist[i+1][j]:
                tempWord = wordlist[i][j]
                tempCount+=1
            else:
                tempWord = '?'
        if tempCount ==N-1:
            result += tempWord
        else:
            result += '?'
    print(result)