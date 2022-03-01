# 전화번호 버튼에는 2에서 9까지의 숫자가 주어져있고 해당되는 알파벳이 다음과 같다.
# 전화번호로 조합 가능한 모든 문자를 출력하라.
# 주어진 3가지 전화번호로 조합 가능한 문자를 출력해보자

phoneNumber = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
# 입력한 번호
inputNumbers = [3, 7, 4]
result = []
# print(phoneNumber[2])
MadeLetters=[]
def makeCombination(index, MadeLetters):
    global result
    # 백트래킹 부분
    # 가지치기
    if index == len(inputNumbers):
        x = ""
        for i in MadeLetters:
            x += i
        result.append(x)
        # return result

    else:
        #
        i = inputNumbers[index]

        for char in phoneNumber[i]:
            MadeLetters += char
            makeCombination(index+1, MadeLetters)
            MadeLetters.pop()
    return result

print(makeCombination(0, MadeLetters))
# print(len(set(result)))
# print(result)
# #     for i in inputNumbers:
# #         if phoneNumber[i][char] in phoneNumber[I]:
# #             break
# #         else:
# #             for char in range(len(phoneNumber[i])):
# #                 numbers.append()
# #                 makeCombination()



