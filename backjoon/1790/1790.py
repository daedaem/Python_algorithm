import sys
sys.stdin = open('1790.txt')

N, K = map(int, input().split())
# print(N, K)
result = ''
# 1~9 9 개 *1      9 total 9*1
# 10~ 99 90개 *2    180  total 189 9*21 111
# 100~ 999  900개 * 3    2700 + total 2889 9*321
# 1,000~ 9,999 9000개 * 4 길이     ===   앞까지 결과 + 길이*입력값에서 앞까지 결과빼고(=)

#길이-1까지의 핪 계산하기 100이라면 3글자 1,2
quo = len(str(N))
temp =0
sum =0
prev_max = ''
# quo
for i in range(1, quo+1):
    temp = 9*10**(i-1)*i
    sum += temp
    prev_max += '9'
# print(prev_max)

total = sum + (N-int(prev_max))*quo
# print(total)
if total < K:
    print(-1)
else:
    ## 1~9까지 자기 숫자 10~ 99까지는 홀수가 일의자리 1씩 차이
    # (32 2 , 33 1) (34 2 35 2)
    # (250 1, 251 2,  252 0)
    # (2884, 9, 2885, 9   2886,8), (2887, 9, 2888, 9   2889,9)
    # 1~9지자리 9까지
    # 10~99  90까지 9+ 1n, 2n 1이 십의자리
    # 100~ 999까지  이전까지 총길이 빼고 3으로 나눠서
    # 1,000 ~ 9999까지 9,000 *4
    #
    # 23 - 9 =14
    # 1*9 + 2* 90 = 3 * 900
    #  9 180 2700
    # 2600
    # 길이로 나누고 str로 바꾼다음 몇번째

    if K < 10:
        print(K)
    else:
        K_len = len(str(K))-1
        print(K_len)
        # 1~9 9 개 *1      9 total 9*1 1
        # 10~ 99 90개 *2    180  total 189 9*21 9*(10 + 10+1) 189번째까지는 2자리수
        # 100~ 999  900개 * 3    2700 + total 2889 9*321 9*( 3*100+ 2*10+ 1*1) 1800 200   2889번쨰까지는 3자리수 k
        n = 0
        sum = 0
        temp = 0
        valuelist=[]
        result = []
        prev_value = 0
        temps = 0
        value = 0
        # 몇글자 인지 확인 K 9 + 189 2700 2890 2889 temp 0 n2 sum 0
        # n = 글자수, sum n번째 글자수 마지막까지의 총번째 수, 그 값은 10**n
        while K > sum:
            prev_value += int(9 * (10 ** (n-1)))//10
            sum += temp
            temp = 0
            n += 1
            temp = 9*((10 ** (n-1)) * n)
            value += 9*(10**(n-1))
            result.append(sum)
            valuelist.append(value)
        #
        print(result)
        print(valuelist)
        n = n-1
        print(n)
        #
        # print(n) # n은 현재자리수
        # # 과거자리수 = n-1
        # # 과거자리값 = valuelist[과거자리수-1]
        # # print(과거자리값)
        # 현재자리값 = 과거자리값 + ((K - result[- 1]) // n)
        # # print(현재자리값)
        # # if 과거자리값 + ((K - result[n - 1]) // n)% n :
        # #     현재자리값 = 과거자리값 + ((K - result[n - 1]) // n)+1
        # # else:
        # #     현재자리값 = 과거자리값 + ((K - result[n - 1]) // n)
        # # print(현재자리값)
        # print(str(현재자리값)[(K - result[n - 1]) %n])
