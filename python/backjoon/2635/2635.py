import sys
sys.stdin = open('2635.txt')


N = input(int())
M = 1
newlist = [N. M]
newlist.append(M)
#함수 끝이나면
    for i in range(M):
        x = newlist [M-2] - newlist[M-1]
        append(x)

# while result가 0보다 큰 동안에
# 두번째 수를 계속 생성해본다 0부터 해보면 되겠지
# 먼저 길이가 1일 때는 무시
# 길이가 2이상일 때부터는 세번째항인 [N] = [N-2] - [N-1]
# N을 다시 리스트에 추가 인덱스 N은 다시 더 뒤로 움직이고
#
# 함수
# 다 돌고나서 마지막에 append
# #함수외
# def rules(N, M):
#     result = newlist[N-2]- newlist[N-1]
#     rules(N) =results
#     return
#
#
#     # len()
#
#     M = M+1 # 마지막에 M플러스1로 리턴해본다
#     retrun rules(N, M=1)

N = input(int())
M = 1
newlist.append(M)
#함수 끝이나면
while M < N:
    M += 1


# 길이값 최대와 그 안에 원소들같이 출력
