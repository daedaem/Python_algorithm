import sys
sys.stdin = open('7568.txt')
N = int(input())
people = [list(map(int,input().split())) for _ in range(N)]
# print(people)
visited = [0]*N
record = [1] *N
temp = 0
def dfs(i, depth, temp):
    global record
    if depth == 2:
        if people[i][0] > people[temp][0] and people[i][1] > people[temp][1]:
            record[temp]+=1
        elif people[i][0] < people[temp][0] and people[i][1] < people[temp][1]:
            record[i] +=1
        elif people[i][0] < people[temp][0] and people[i][1] > people[temp][1]:
            pass
            # record[temp] += 1
            # record[i] +=1
        elif people[i][0] > people[temp][0] and people[i][1] < people[temp][1]:
            pass
            # record[temp] += 1
            # record[i] +=1
    else:
        for y in range(i, N):
            if visited[y] == 1:
                pass
            else:
                visited[y] = 1
                temp = y
                dfs(i, depth+1, y)
                visited[y] =0
                # temp = 0
for i in range(N):
    # visited[i]=1
    dfs(i, 1, 0)
    # visited[i] = 0
print(*record)
# for i in range(N-1):
    # if people[i][0]> people[i+1][0] and people[i][1]> people[i+1][1]:
# people = sorted(people)[::-1]
# print(people)
# for