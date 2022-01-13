import sys
sys.stdin = open('12933.txt')

sound = input()
y = sound.split('quack')
# print(sound.count('quack'))
# print(y)
x = ['q','u','a','c','k']
cnt = 0
mins = 2500/4
stack = []
result = []
temp =''
for i in range(len(sound)):
    # 첫시작이 q이면 temp추가
    # 아니면 stack에 추가
    if temp =='':
        if sound[i] == 'q':
            temp += 'q'
        else:
            stack.append(sound[i])
    else:
        if sound[i] =='q'

    if temp =='quack':
        result.append('quack')
        temp = ''
    # print(temp)





# quack으로 정확하게 끊어지는 게 없으면
# if 'quack' not in sound:
#     # quack의 총 숫자
#     totals = int(len(sound)/10)
#     print(int(totals))
# if 'quack' in sound:
#     totals = int(len(sound) / 5)
#     print(totals - y.count(''))
# print(mins)
# print(y.count(''))

