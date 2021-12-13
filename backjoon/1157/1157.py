# chr(122)) #65 A a 97 90Z z122  +32
import sys
sys.stdin = open('1157.txt')
# 알파벳 대소문자 구분 없으니 아스키 코드 이용해보자
# 세트로 중복되는 문자제거하고 그안에서 문자 꺼내서 찾는데 이용하자
# 알파벳 소문자와 대문자 합친 sum을 비교해서 더크면 알파벳 바꾼다.
# 근데 만약에 수가 동일하다 바로 ?출력하고 break
words = list(input())
wordlist = set(words)
# 중복 제거 및 찾아야할 문자들
findlist = list(wordlist)
# print(words)
# print(wordlist)
# print(findlist)
tempnum = []
tempword = []
# 리스트에서 중복되는거 골라주는 과정
for i in findlist:
    if chr(ord(i) + 32) in findlist:
        findlist.remove(chr(ord(i) + 32))
    if chr(ord(i) - 32) in findlist:
        findlist.remove(chr(ord(i) - 32))
# print(findlist)

for i in findlist:
    if ord(i) > 96:
        chg = chr(ord(i) - 32)
        tempword.append(i)
        tempnum.append(words.count(i) + words.count(chg))
    else:
        chg = chr(ord(i) + 32)
        tempword.append(i)
        tempnum.append(words.count(i) + words.count(chg))

if tempnum.count(max(tempnum)) >= 2:
    print('?')
else:
     x = tempnum.index(max(tempnum))
     result = tempword[x]
     if ord(result) > 96:
         result = chr(ord(result) - 32)
         print(result)
     else:
         print(result)
