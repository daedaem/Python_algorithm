import sys
sys.stdin = open('12874.txt')
n, m = map(int, input().split())
salary = list(map(int, input().split()))
max_value = 0
temp=0
for i in range(m):
    temp += salary[i]
# print(temp)
if m ==1:
    print(max(salary))
elif n==m:
    print(sum(salary))
else:
    for i in range(n-m):
        if max_value <= temp:
            max_value = temp
        temp = temp - salary[i] + salary[i + m]
    print(max_value)

    # for j in range(m):
    #     temp += salary[i+j]
    # if temp >= max_value:
    #     max_value=temp
