import sys
sys.stdin = open("1316.txt")
n = int(input())
result = 0
for i in range(n):
    cnt = 0
    wordlist = input()
    for a in range(len(wordlist)-1):
        if wordlist[a] != wordlist[a+1]:
            if wordlist[a] in wordlist[wordlist.index(wordlist[a+1]):]:
                cnt +=1
    if cnt >= 1:
        pass
    else:
        result += 1
print(result)