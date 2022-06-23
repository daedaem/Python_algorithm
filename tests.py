import sys
# sys.setrecursionlimit(10**7)
def solution(N, fees, dest):
    record = list([0 for _ in range(N+1)] for _ in range(N+1))
    # print(record)
    nodeinfo = [[] for _ in range(N+1)]
    for i in fees:
        record[i[0]][i[1]] = i[2]
        record[i[1]][i[0]] = i[2]
        # print(i[0])
        nodeinfo[i[0]].append(i[1])
        nodeinfo[i[1]].append(i[0])
    # print(record)
    print(nodeinfo)
    minn=10e10
    # print(minn)
    visited = [0 for _ in range(N+1)]
    def dfs(start):
        # if sum(visited)==
        if start == dest:
            if sums< minn:
                minn = sums
                return minn
            else:
                return minn
        else:
            for i in nodeinfo[start]:
                visited[i] = 1
                dfs(i)
                # visited[i]=0
    print(dfs(1))
    answer = 0
    return answer

N = 5
fees = [[1, 2, 1000], [1, 5, 2000], [2, 3, 3000], [2, 4, 1500], [3, 4, 1000], [4, 5, 2000]]
dest = 3
