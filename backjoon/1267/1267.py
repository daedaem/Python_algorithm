import sys
sys.stdin=open('1267.txt')
for tc in range(1, 3):
    V, E = map(int, input().split())
    print(V, E)
    orders = list(map(int, input().split()))
    print(orders)
    record = [0 for _ in range(V+1)]
    print(record)
    1 4 2 3