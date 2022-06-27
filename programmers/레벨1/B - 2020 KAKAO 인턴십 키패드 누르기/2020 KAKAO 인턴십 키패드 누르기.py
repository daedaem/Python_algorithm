def solution(numbers, hand):
    answer = ''
    keyPad = [[1,2,3], [4,5,6], [7,8,9], ['*', 0,'#']]
    posNum = dict()
    leftThumb = [3,0]
    rightThumb = [3,2]
    for number in numbers:
        for h in range(4):
            for c in range(3):
                if keyPad[h][c]==number:
                    posNum[number]=[h, c]
            #     왼쪽사이드면
                    if c ==0 and h<3:
                        answer+='L'
                        leftThumb = [h,c]
                    elif c== 2 and h<3:
                        answer+='R'
                        rightThumb = [h,c]
                    elif c==1:
            #             같을때
                        if abs(leftThumb[0]- h) + abs(leftThumb[1] - c) == abs(rightThumb[0]- h) + abs(rightThumb[1] - c):
                            if hand=="right":
                                answer+='R'
                                rightThumb = [h,c]
                            else:
                                answer+='L'
                                leftThumb = [h,c]
                        elif abs(leftThumb[0]- h) + abs(leftThumb[1] - c) < abs(rightThumb[0]- h) + abs(rightThumb[1] - c):
                            answer+='L'
                            leftThumb = [h,c]
                        else:
                            answer+='R'
                            rightThumb = [h,c]
    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = 'right'
solution(numbers, hand)

# def solution(numbers, hand):
#     answer = ''
#     left = [1,4,7]
#     right = [3,6,9]
#     center = [2,5,8,0]
#     keyPad= [[1,2,3],[4,5,6],[7,8,9],['*',0,"#"]]
#     prevL = [3, 0]
#     prevR = [3, 1]
#     for i in numbers:
#         for j in range(4):
#             for c in range(3):
#                 if keyPad[j][c] == i:
#                     if c==0:
#                         prevL = [j, c]
#                     elif c==2:
#                         prevR = [j, c]
#                     # 중간이면
#                     else:
#                         pass
#                 else:
#                     pass
#
#
#
#
#
#         if i in keyPad[0]:
#             answer += 'L'
#             prevL = i
#         elif i in keyPad[1]:
#             answer += 'R'
#             prevR = i
#         else:
#
#     return answer