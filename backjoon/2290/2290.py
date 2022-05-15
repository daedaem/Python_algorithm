import sys
sys.stdin=open('2290.txt')
s, n = map(int,input().split())
n=str(n)
# zero=[' ' + '-'*s + ' '+'\n'+ ('|'+' '*s+ '|'+'\n')*((2*s+2)//2-1)+('\n'+'|'+' '*s+ '|')*((2*s+2)//2-1)+ ("\n"+ ' ' + '-'*s + ' ')]
# one=[" "*(s+2)+'\n'+(" "*(s+1)+'|'+'\n')*((2*s+2)//2-1)+" "*(s+2)+('\n'+" "*(s+1)+'|')*((2*s+2)//2-1)+'\n'+" "*(s+2)]
# two=[' ' + '-' * s + ' '+('\n'+' '*(s+1)+ '|')*((2*s+2)//2-1)+'\n' +' ' + '-'*s + ' '+('\n'+'|'+' '*(s+1))*((2*s+2)//2-1)+'\n'+ ' ' + '-'*s + ' ']
# three=[' ' + '-'*s + ' '+('\n'+' '*(s+1)+ '|')*((2*s+2)//2-1)+'\n'+' ' + '-'*s + ' '+('\n'+' '*(s+1)+ '|')*((2*s+2)//2-1)+'\n'+(' ' + '-'*s + ' ')]
# four=[' '*(s+2)+ '\n'+('|'+' '*s+ '|'+'\n')*((2*s+2)//2-1)+ ' ' + '-'*s + ' '+ ('\n'+' '*(s+1)+ '|')*((2*s+2)//2-1)]
# five=[(' ' + '-'*s + ' '+ ('\n'+'|'+' '*(s+1))*((2*s+2)//2-1)+'\n'+' ' + '-'*s + ' '+('\n'+' '*(s+1)+ '|')*((2*s+2)//2-1)+'\n'+' ' + '-'*s + ' ')]
# six=[' ' + '-'*s + ' '+('\n'+'|'+' '*(s+1))*((2*s+2)//2-1)+'\n'+' ' + '-'*s + ' '+('\n'+'|'+' '*s+ '|')*((2*s+2)//2-1)+'\n'+' ' + '-'*s + ' ']
# seven=[' ' + '-'*s + ' '+('\n'+' '*(s+1)+ '|')*((2*s+2)//2-1)+'\n'+' ' *(s+2)+('\n'+' '*(s+1)+ '|')*((2*s+2)//2-1)+'\n'+' ' *(s+2)]
# eight=[' ' + '-'*s + ' '+('\n'+'|'+' '*s+ '|')*((2*s+2)//2-1)+'\n'+' ' + '-'*s + ' '+('\n'+'|'+' '*s+ '|')*((2*s+2)//2-1)+'\n'+' ' + '-'*s + ' ']
# nine=[' ' + '-'*s + ' '+('\n'+'|'+' '*s+ '|')*((2*s+2)//2-1)+'\n'+' ' + '-'*s + ' '+('\n'+' '*(s+1)+ '|')*((2*s+2)//2-1)+'\n'+' ' + '-'*s + ' ']
# zero = [(' ' + '-'*s + ' '),(('|'+' '*s+ '|'+'\n')*((2*s+2)//2-1)),(" "*(s+2)), (('\n'+'|'+' '*s+ '|')*((2*s+2)//2-1)),(' ' + '-'*s + ' ')]
# one = [(" "*(s+2)),(" "*(s+1)+'|')*((2*s+2)//2-1),(" "*(s+2)),((" "*(s+1)+'|')*((2*s+2)//2-1)),(" "*(s+2))]
# result = []
# for i in range(len(str(n))):
#     if int(n[i])==0:
#         for i in range(2 * s + 3):
#             if i == 0 or i == 2 * s + 2:
#                 result.append((" " + "-" * s + ""))
#             elif i == s + 1:
#                 result.append((" " * (s + 2)))
#                 # print(i)
#             else:
#                 # print(i)
#                 result.append(("|" + " " * s + "|"))
#     elif int(n[i])==1:
#         for i in range(2*s+3):
#             if i ==0 or i == 2*s+2 or i ==s+1:
#                 result.append((" "*(s+2)))
#                 # print(i)
#             else:
#                 # print(i)
#                 result.append((" "*(s+1)+'|'))
# for i in result:
#     print(i)
# print(result)
# 중앙이 (" "*(s+2))이면 print 다음 end=""로변경
# print(zero[0], end='\n', zero[1])
# for i in range(2):
#     for j in range(5):
#         pass
# print(*zero)
# result =[]
# result.append(zero)
# result = [zero, one]
# for i in range(len(result)):
#     for j in range(len(result[i])):
#         print(result[i][j])
    # for j in range(5):
    #     print(*i[j], end="")
        # print()

    # print(i)

# print(*one)
# print(*zeroList)
# print(*oneList)
# print(*twoList)
# 항상 끝이 한칸 더 있어서 맨밑에 개행문자 뺐는데
# 혹시 안되면 원상복귀
# 노가다로 다 만든 다음 시작
# for i in range(len(str(n))):
#     if int(n[i])==0:
#         print(*zero, end="")
# #     # 0이면
# #         print(' ' + '-'*s + ' ')
# #         print(('|'+' '*s+ '|'+'\n')*((2*s+2)//2-1), end="")
# #         print(('\n'+'|'+' '*s+ '|')*((2*s+2)//2-1))
# #         print(' ' + '-'*s + ' ')
#     elif int(n[i])==1:
#         # print(*one, end="")
#         print(" "*(s+2))
#         print((" "*(s+1)+'|'+'\n')*((2*s+2)//2-1))
#         print(" "*(s+2))
#         print(('\n'+" "*(s+1)+'|')*((2*s+2)//2-1))
# #         print(" "*(s+2))
#     elif int(n[i])==2:
#         print(*two, end="")
# #         print(' ' + '-' * s + ' ', end="")
# #         print(('\n'+' '*(s+1)+ '|')*((2*s+2)//2-1))
# #         print(' ' + '-'*s + ' ', end="")
# #         print(('\n'+'|'+' '*(s+1))*((2*s+2)//2-1))
# #         print(' ' + '-'*s + ' ')
#     elif int(n[i])==3:
#         print(*three, end="")
# #         print(' ' + '-'*s + ' ', end="")
# #         print(('\n'+' '*(s+1)+ '|')*((2*s+2)//2-1))
# #         print(' ' + '-'*s + ' ', end="")
# #         print(('\n'+' '*(s+1)+ '|')*((2*s+2)//2-1))
# #         print(' ' + '-'*s + ' ')
#     elif int(n[i])==4:
#         print(*four, end="")
# #         print(' '*(s+2))
# #         print(('|'+' '*s+ '|'+'\n')*((2*s+2)//2-1), end="")
# #         print(' ' + '-'*s + ' ', end="")
# #         print(('\n'+' '*(s+1)+ '|')*((2*s+2)//2-1))
# #         print(' '*(s+2))
#     elif int(n[i])==5:
#         print(*five, end="")
# #         print(' ' + '-'*s + ' ', end="")
# #         print(('\n'+'|'+' '*(s+1))*((2*s+2)//2-1))
# #         print(' ' + '-'*s + ' ', end="")
# #         print(('\n'+' '*(s+1)+ '|')*((2*s+2)//2-1))
# #         print(' ' + '-'*s + ' ')
#     elif int(n[i])==6:
#         print(*six, end="")
# #         print(' ' + '-'*s + ' ', end="")
# #         print(('\n'+'|'+' '*(s+1))*((2*s+2)//2-1))
# #         print(' ' + '-'*s + ' ', end="")
# #         print(('\n'+'|'+' '*s+ '|')*((2*s+2)//2-1))
# #         print(' ' + '-'*s + ' ')
#     elif int(n[i])==7:
#         print(*seven, end="")
# #         print(' ' + '-'*s + ' ', end="")
# #         print(('\n'+' '*(s+1)+ '|')*((2*s+2)//2-1))
# #         print(' ' *(s+2), end="")
# #         print(('\n'+' '*(s+1)+ '|')*((2*s+2)//2-1))
# #         print(' ' *(s+2))
#     elif int(n[i])==8:
#         print(*eight, end="")
# #         print(' ' + '-'*s + ' ', end="")
# #         print(('\n'+'|'+' '*s+ '|')*((2*s+2)//2-1))
# #         print(' ' + '-'*s + ' ', end="")
# #         print(('\n'+'|'+' '*s+ '|')*((2*s+2)//2-1))
# #         print(' ' + '-'*s + ' ')
#     elif int(n[i])==9:
#         print(*nine, end="")
# #         print(' ' + '-'*s + ' ', end="")
# #         print(('\n'+'|'+' '*s+ '|')*((2*s+2)//2-1))
# #         print(' ' + '-'*s + ' ', end="")
# #         print(('\n'+' '*(s+1)+ '|')*((2*s+2)//2-1))
# #         print(' ' + '-'*s + ' ')
# 맨끝 순서는 일단 제외하고 다 뒤에 띄우기
#     if i==len(str(n)):
#         pass
#     if i != len(str(n))-1:
#         print((''+'\n')*(s*2+3), end="")
