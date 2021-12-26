import sys
sys.stdin=open('1620.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
dogam = dict()
reverse_dogam = dict()
for i in range(1, N+1):
    dogam[i] = input().rstrip()
# print(dogam)
reverse_dogam = {v:k for k,v in dogam.items()}
# print(reverse_dogam)
for i in range(1, M+1):
    x = input().rstrip()
    # print(x)
    if x.isalpha():
        print(reverse_dogam[x])
    elif x.isdigit():
        print(dogam[int(x)])
# print(wordlist)
# dogam = {num: i+1 for i,num in enumerate(wordlist)}


# for i in problems:
#     if i.isalpha():
#         # print(1)
#         print(dogam)
#     elif i.isdigit():
#         # print(2)
#         print(reverse_dogam[i])
