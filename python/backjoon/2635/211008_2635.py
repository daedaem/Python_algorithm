import sys
sys.stdin=open('2635.txt', 'r')

n = int(input())
#두번째 수 cnt
cnt = 1
n_1 = 1
max = 0
# 최종 각 리스트들을 담을 결과리스트 result
result = []
#임시적으로 해당되는 수를 넣을 변수 temp
#만약 이게 젤 크면 변수와 그 길이 담기
temp=[]
max=0
maxlist=[]
while n >= cnt:
    if n - cnt < 0:
        temp=[n]
        pass
    else:
        temp = [n, cnt]
        while n_1 >= 0:
            n_1 = temp[-2] - temp[-1]
            if n_1 < 0:
                n_1 = 1# 이부분때문에 막힘
                break
            else:
                temp.append(n_1)
        # print(temp)
        if max < len(temp):
            max = len(temp)
            maxlist = temp
        else:
            pass
    cnt+=1
result += max, *maxlist
print(result[0])
print(*result[1:])

