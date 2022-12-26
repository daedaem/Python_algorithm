import sys
sys.stdin = open("5622.txt")
dial = [[], [], [], ['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'], ['M', 'N', 'O'],
        ['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]
wordlist = input()
cnt = 0
for i in wordlist:
    for j in range(len(dial)):
        if i in dial[j]:
            cnt+=j
print(cnt)