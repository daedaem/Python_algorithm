# 일단 모든 인풋들을 스택에다가 담는다.
# 근데 push의 경우 리스트 안에 push와 숫자변수에 따로 담는다
#  나머지는 그대로

N = int(input())
stack = []
wordlist = []
for _ in range(N):
    word = input()
    if ' ' in word:
        x = word.split()
        # print(x)
        wordlist.append(x[0])
        wordlist.append(x[1])
    else: wordlist.append(word)

    # print(wordlist)
    for i in wordlist:
        if i == 'top':
            print(stack[-1])
            wordlist.pop(0)    
        else:
            print(-1)
            wordlist.pop(0) 
 
        if i == 'size':
            print(len(stack))
            wordlist.pop(0)   

        elif i == 'pop':
            if not stack:
                print(-1)
                wordlist.pop(0)   
            else:
                print(stack.pop())
                wordlist.pop(0)   
        
        elif i == 'empty':
            if not stack:
                print(1)
                wordlist.pop(0)   
            else:
                print(0)
                wordlist.pop(0)   
        
        elif i == 'push':
            wordlist.pop(0)
            x= wordlist.pop(0)
            stack.append(int(x))