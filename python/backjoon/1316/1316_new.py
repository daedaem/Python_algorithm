import sys
sys.stdin = open('1316.txt')

N = int(input())
count = 0
for _ in range(N):
    # 단어 하나씩 받고
    words = input()
    # 1. 현재 단어 result 세트에 담고
    result = set()
    # 현재단어를 기입할 temp
    temp = ''
    # 한개면 무조건 맞으니까 +1
    if len(words) == 1:
        count += 1
    # 일단 +1하고
    else:
        # count += 1
        for i in range(1, len(words)):
            # 세트는 중복해결되니까 일단 추가
            result.add(words[i-1])
            # 그다음 단어랑 현재랑 다를때,
            if words[i]!=words[i-1]:
                # 다음 단어가 현재글자들이 담겨있는 result에 있으면 더한거 취소
                if words[i] in result:
                    count -= 1
                    break
print(count)
