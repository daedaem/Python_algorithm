def solution(numbers, hand):
    answer = ''
    left = [1,4,7]
    right = [3,6,9]
    center = [2,5,8,0]
    posNumber = [[3,1], [0,0],[0,1],[0,2], [1,0], [1,1], [1,2], [2,0], [2,1], [2,2]]
    prevL = ''
    prevR = ''
    for i in numbers:
        # 숫자가 left에 있으면
        if i in left:
            answer+='L'
            prevL = i
        # 숫자가 right에 있으면
        elif i in right:
            answer+='R'
            prevR = i
        # 숫자가 center에 있으면
        elif i in center:
#             만약 이전에 누른 번호가 없으면
# 있다가 확인해보자 둘중에 하나만 올려져 있으면
            # 둘다 안눌려져있으면
            if not prevL and not prevR:
                if hand == "right":
                    answer+='R'
                    prevR = i
                else:
                    answer+='L'
                    prevL = i
#          둘다 있을 때
            elif prevL and prevR:
#             길이가 같으면
                if abs(posNumber[prevL][0] - posNumber[i][0]) + abs(posNumber[prevL][1]-posNumber[i][1]) == abs(posNumber[prevR][0] - posNumber[i][0]) + abs(posNumber[prevR][1]-posNumber[i][1]):
#                   길이는 같은데 오른손잡이면
                    if hand == "right":
                        answer+='R'
                        prevR = i
#                   길이는 같은데 왼손잡이면
                    else:
                        answer+='L'
                        prevL = i
#              왼쪽이 더 가까우면
                elif abs(posNumber[prevL][0] - posNumber[i][0]) + abs(posNumber[prevL][1]-posNumber[i][1]) < abs(posNumber[prevR][0] - posNumber[i][0]) + abs(posNumber[prevR][1]-posNumber[i][1]):
                    answer+="L"
                    prevL = i
#              오른쪽이 더 가까우면
                else:
                    answer+="R"
                    prevR = i
#           둘중 하나만 있을 때
            else:
                if prevL and not prevR:
                    prevR=[3,2]
                    if abs(posNumber[prevL][0] - posNumber[i][0]) + abs(posNumber[prevL][1]-posNumber[i][1]) == abs(prevR[0] - posNumber[i][0]) + abs(prevR[1]-posNumber[i][1]):
                        if hand=="right":
                            answer+="R"
                            prevR = i
                        else:
                            answer+="L"
                            prevL = i
                    elif abs(posNumber[prevL][0] - posNumber[i][0]) + abs(posNumber[prevL][1]-posNumber[i][1]) < abs(prevR[0] - posNumber[i][0]) + abs(prevR[1]-posNumber[i][1]):
                        answer+="L"
                        prevL = i
                    else:
                        answer+='R'
                        prevR = i
#               왼쪽은 없고 오른쪽만 있을 때
                elif not prevL and prevR:
                    prevL= [3,0]
                    if abs(prevL[0] - posNumber[i][0]) + abs(prevL[1]-posNumber[i][1]) == abs(posNumber[prevR][0] - posNumber[i][0]) + abs(posNumber[prevR][1] - posNumber[i][1]):
                        if hand=="right":
                            answer+="R"
                            prevR = i
                        else:
                            answer+="L"
                    elif abs(prevL[0] - posNumber[i][0]) + abs(prevL[1]-posNumber[i][1]) < abs(posNumber[prevR][0] - posNumber[i][0]) + abs(posNumber[prevR][1] - posNumber[i][1]):
                        answer+="L"
                        prevL = i
                    else:
                        answer+='R'
                        prevR = i
    return answer