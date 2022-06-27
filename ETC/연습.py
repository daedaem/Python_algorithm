
def solution(number, k):
    answer = ''
    number = list(map(int, list(number)))
    drawNumber = len(number) - k
    temp = ''
    maxNumber = 0

    visited = [0 for _ in range(len(number))]
    temp = []

    def dfs(n):
        global maxNumber, words
        maxNumber = 0
        words = ''
        if len(n) == drawNumber:
            if maxNumber <= int(n):
                maxNumber = int(n)
                temp.append(maxNumber)
                print(temp)
        else:
            for i in range(len(number)):
                if visited[i] ==1:
                    pass
                else:
                    visited[i]=1
                    words += number[i]
                    dfs(words)
        return temp
    dfs('')

    return answer