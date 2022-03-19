# # 1번째 답
# import sys
# lines = 1
# result = []
# lines = sys.stdin.readlines()
# print(lines)
# print(lines[0])

# 2번째 답
import sys
sys.stdin=open('10951.txt')
# result = 1
while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except: 
        break

