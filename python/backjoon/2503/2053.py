import sys
sys.stdin = open('2503.txt')

N = int(input())
checkProblem = [input().split() for _ in range(N)]
# print(checkProblem)
checkProblem[0] = list(checkProblem[0])
# 2스트라이크, 1스트라이크 1볼, 2볼인거부터
# 2개면 비교.
temp = []
result = []
visited = [0] * 10
anscount = 0
finalcount=0
# print(visited)
for i in range(1, 10):
    visited = [0] * 10
    temp = []
    visited[i] = 1
    temp.append(i)
    for j in range(1, 10):
        if visited[j] == 1:
            continue
        else:
            visited[j] = 1
            temp.append(j)
        for z in range(1, 10):
            if visited[z] == 1:
                continue
            else:
                temp.append(z)
                candidate = str(temp[0]) + str(temp[1]) + str(temp[2])
                anscount = 0
                for v in range(N):
                    strike = 0
                    ball = 0
                    for c in range(3):
                    # 후보군이랑 체킹해야할 숫자가 같으면
                        if candidate[c] == checkProblem[v][0][c]:
                            strike +=1
                        elif candidate[c] != checkProblem[v][0] and candidate[c] in checkProblem[v][0]:
                            ball +=1
                    if int(checkProblem[v][1]) == strike and int(checkProblem[v][2]) == ball:
                        anscount+=1
                if anscount == N:
                    finalcount += 1
                        # if checkProblem[v][1] ==3 and checkProblem[v][2] ==0:
                        #     anscount +=1
                temp.pop()
        visited[j] = 0
        temp.pop()
print(finalcount)