import sys
sys.stdin = open('3052.txt')

arr = set()
numbers = sys.stdin.readlines()
for num in numbers:
    num = (int(num.split()[0])) % 42
    arr.add(num)

# while True:
#     try:
#         num = int(input())
#         num %= 42
#         arr.add(num)
#     except EOFError:
#         break
print(len(arr))
    