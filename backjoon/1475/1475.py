#6or9한개 69가 한 세트   69. 99 66 전부 한개
# 3개면  696 699 999 666 669 2개 6666 6669 6699 6999 9999 2개
# 66 6 or 9 홀수씩 이면  1개 6699 2개 6691 2개 홀수라도 3이면 2개
# 66666 66669 66699 3개 갯수는 69 총합 갯수 69개수가 2로 나눴을때. 홀수면 몫 +1 짝수면 몫
import sys
sys.stdin = open('1475.txt')
x = list(map(int, input()))
sum = 0
sumsixnine = 0

# 리스트 길이 재고 6과 9 갯수 도출한다음 길이에서 빼고
# 6,9 세트 구한 값을 더해준다.
### 6, 9 둘 중에 하나로 통일
### 1세트 사용했으면 체크 0~8
# [1 3 4 0 2 0 0 0 0 0 ]
for j in range(len(x)):
    if j == 6 or 9:

    if x.count(j) >= 2:
        sum += x.count(j)-1
    if x[j] == 6 or x[j] == 9:
        sumsixnine += 1
    else:
        sum += 1
# print(sum)
# print(sumsixnine)
if sumsixnine % 2:
    y = sumsixnine // 2 + 1
if sumsixnine % 2 == 0:
    y = sumsixnine // 2
result = y + sum
print(result)

# 6이나 9가 아니고  count가 2개이상이면  count = 1
#
#     for i in range(10):
#         if i in x:
#             if i == 6 or i == 9:
#                 sumsixnine += x.count(i)
#             else:
#                 sum += x.count(i)
#         else:
#             pass
# if sumsixnine !=0 and sumsixnine % 2:
#     y = sumsixnine //2 +1
# if sumsixnine !=0 and sum % 2 == 0 :
#     y = sumsixnine // 2
# if sumsixnine ==0:
#     y = 0
# result = y + sum
# print(result)

# y = x.count(6) + x. count(9)
# print(y)