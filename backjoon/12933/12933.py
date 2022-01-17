import sys
sys.stdin = open('12933.txt')

# 문제해결법
# quack가 완성될때까지 q갯수 찾기하고 없애고
# max_count에 적은다음
# 그 뒤에 또 부분에서 quack 완성 될 때까지 q 갯수 찾기해서 max_count 보다 크면 변경하고 출력

soundlist = list(input())
# 임시적으로 체크해줄 똑같은 sounds 변수 생성
sounds = soundlist.copy()
maxcount = 0
stack = []
temp=''
result1 = 0
if soundlist.count('q') == soundlist.count('u') == soundlist.count('a') == soundlist.count('c') == soundlist.count('k'):
    while sounds:
        if sounds and sounds[0]!='q':
            break
        stack = []
        for i in range(len(sounds)):
            if i ==0 and sounds[i] != 'q':
                break
            if temp=='':
                if sounds[i] =='q':
                    temp+='q'
                    sounds[i]=0
                else:
                    stack.append(sounds[i])
            elif temp == 'q':
                if sounds[i] == 'u':
                    temp+='u'
                    sounds[i]=0
                else:
                    stack.append(sounds[i])
                    # sounds.pop(0)
                    # sounds.append(i)
            elif temp == 'qu':
                if sounds[i] == 'a':
                    temp += 'a'
                    sounds[i]=0
                else:
                    stack.append(sounds[i])
                    # sounds.pop(0)
                    # sounds.append(i)
            elif temp == 'qua':
                if sounds[i] == 'c':
                    temp += 'c'
                    sounds[i]=0
                else:
                    stack.append(sounds[i])
                    # sounds.pop(0)
                    # sounds.append(i)
            elif temp == 'quac':
                if sounds[i] == 'k':
                    temp += 'k'
                    sounds[i]=0
                else:
                    stack.append(sounds[i])
                    # sounds.pop(0)
                    # sounds.append(i)
            if temp =='quack':
                temp =''
        else:
            sounds = stack.copy()
        # stack = []
    # print(sounds)
    if not sounds:
        while 'q' in soundlist:
            start = soundlist.index('q')
            end = soundlist.index('k')
            new_soundlist = soundlist[start:end + 1]
            if new_soundlist.count('q') >= maxcount:
                maxcount = new_soundlist.count('q')
            else:
                pass
            soundlist[start] = 0
            soundlist[end] = 0
        print(maxcount)
    else:
        print(-1)
else:
    print(-1)

# temp =''
# for i in range(len(sound)):
    # print(sound[i])
    # quaquckqauckack
    # quack 3
    # quack 3
    # qua
    # q


# while soundlist:
#     x = soundlist.pop(0)
#     # stack.append(x)
#     if temp == '':
#         if x== 'q':
#             temp += x
#         else:
#             soundlist.append(x)
#     elif temp == 'q':
#         if x== 'u':
#             temp += x
#         else:
#             soundlist.append(x)
#     elif temp == 'qu':
#         if x== 'a':
#             temp += x
#         else:
#             soundlist.append(x)
#     elif temp == 'qua':
#         if x== 'c':
#             temp += x
#         else:
#             soundlist.append(x)
#     elif temp == 'quac':
#         if x== 'k':
#             temp += x
#         else:
#             soundlist.append(x)
#     if temp == 'quack':
#         result.append('quack')
#         temp = ''
# print(result)
# print(soundlist)
# print(soundlist.count('q'))
# print(stack)

#     # print('stack은', stack)
#     # print('temp는', temp)
#     if temp =='quack':
        # result.append('quack')
#         temp = ''
#     # 첫시작이 q이면 temp추가
#     # 아니면 stack에 추가
#     if temp =='':
#         if sound[i] == 'q':
#             temp += 'q'
#         else:
#             stack.append(sound[i])
#     # temp에 들어가 있으면
#     else:
#         if temp[-1] == 'q':
#             if sound[i]=='u':
#                 temp += 'u'
#             else:
#                 stack.append(sound[i])
#         elif temp[-1] == 'u':
#             if sound[i]=='a':
#                 temp += 'a'
#             else:
#                 stack.append(sound[i])
#         elif temp[-1] == 'a':
#             if sound[i]=='c':
#                 temp += 'c'
#             else:
#                 stack.append(sound[i])
#         elif temp[-1] == 'c':
#             if sound[i]=='k':
#                 temp += 'k'
#             else:
#                 stack.append(sound[i])
# # 남은 스택에서 시작점이 q가아니라면 잘못된거니까 바로 -1 출력
# print(stack)
# stack2 = []
# if stack and stack[0] !='q':
#     print(-1)
# else:
#     temp = ''
#     while stack:
#         if temp == 'quack':
#             result.append('add')
#             temp = ''
#         if temp == '':
#             x = stack.pop(0)
#             # print(x)
#             if x =='q':
#                 temp += x
#                 stack.insert(0, x)
#             else:
#                 stack.append(x)
#                 break
#         else:
#             x = stack.pop(0)
#             if temp[-1] == 'q':
#                 if  x == 'u':
#                     temp += 'u'
#                 else:
#                     stack.append(x)
#             elif temp[-1] == 'u':
#                 if x == 'a':
#                     temp += 'a'
#                 else:
#                     stack.append(x)
#             elif temp[-1] == 'a':
#                 if x == 'c':
#                     temp += 'c'
#                 else:
#                     stack.append(x)
#             elif temp[-1] == 'c':
#                 if x == 'k':
#                     temp += 'k'
#                 else:
#                     stack.append(x)
#     print(result)
#     cnt2=0
#     realresult =1
#     for i in y:
#         if i != '':
#             cnt2+=1
#         else:
#             realresult = 1
#     realresult += cnt2
#     # print(len(result))
#     print(realresult)




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

