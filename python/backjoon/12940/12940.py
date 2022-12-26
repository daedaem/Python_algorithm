import sys
# from collections import deque
sys.stdin = open("12940.txt")

S = list(input())
T = list(input())

while len(S) != len(T):
    if T[-1] == "A":
        T.pop()
    else:
        T.pop()
        T.reverse()

if T==S:
    print(1)
else:
    print(0)
# dq=deque()

# def BFS():
#     if(S == T):
#         return 1
#     dq.append(S)
#     while dq:
#         word = dq.popleft()
#         if len(word)==len(T):
#             return 0
#         for tp in range(2):
#             if tp:
#                 newword = word+"A"
#             else:
#                 newword = word[::-1] +"B"
#             if(newword==T):
#                 return 1
#             if newword in result:
#                 continue
#             result.add(newword)
#             dq.append(newword)
# print(BFS())
# result = []
# acnt = T.count("A")
# bcnt = T.count("B")
# def dfs(word):
#     if(word.count("A") > acnt or word.count("B")>bcnt):
#         return 0
#     if len(word)== len(T):
#         if word == T:
#             return 1
#         return 0
#     if dfs(word+"A"):
#         return 1
#
#     if dfs(word[::-1]+"B"):
#         return 1
#     return 0
# print(dfs(S))
# print(result)
