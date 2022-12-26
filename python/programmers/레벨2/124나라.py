def solution(n):
    answer = ''
    temp = 1
    results = '1'

    while True:
        allFour = True
        if temp == n:
            break
        else:
            temp += 1
            if len(results) >= 2:
                for i in range(len(results) - 1, -1, -1):
                    if results[i] == '1':
                        results[i] = '2'
                        allFour = False
                        break
                    elif results[i] == '2':
                        results[i] = '4'
                        allFour = False
                        break
                    else:
                        results[i] = '1'
                if allFour == True:
                    results = '1' + results
            else:
                if results == '1':
                    results = '2'
                    allFour = False
                    break
                elif results == '2':
                    results = '4'
                    allFour = False
                    break
                elif results == '4':
                    results = '1'
            if allFour == True:
                results = '1' + results
    print(str(results))
    answer = str(results)
    return answer
solution(3)