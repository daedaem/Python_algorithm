import sys
sys.stdin=open('16922.txt')

numberlist = [1, 5, 10, 50]
# newlist = []
n = int(input())
# print(n)
# 세트로 중복 숫자 해결
result = set()

# 각자 0개 일수 있음
for i in range(n+1):
    for j in range(n-i+1):
        for x in range(n-(i+j)+1):
            for y in range(n-(i+j+x)+1):
                # 근데 합쳐서 n개가 되야하니까 안되면 패스
                if i+j+x+y != n:
                    pass
                # 합쳐서 n개 되면 추가
                else:
                    result.add(i + 5*j + 10* x + 50*y)
print(len(result))
# print(sorted(result))



# # 2개  4-2  5-3
# # 111 115 1110 1150
# sum = []
# temp=0
# collect_number = [0]*n
# for i in range(n): # 0 1 2 3    # 0 1 2 3 4 4
#     for j in range(4):
#         numberlist[i]
#         # for j in range(4): # 이걸 한줄추가불가능
#         print(numberlist[i])
#         # temp += numberlist[i]
#         # print(temp)
#
#     # print(sum)



