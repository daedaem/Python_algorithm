# 전화번호 버튼에는 2에서 9까지의 숫자가 주어져있고 해당되는 알파벳이 다음과 같다.
# 전화번호로 조합 가능한 모든 문자를 출력하라.
# 주어진 3가지 전화번호로 조합 가능한 문자를 출력해보자

phoneNumber = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
# 입력한 번호
inputNumbers = [3, 7, 4]
result = []
# print(phoneNumber[2])
# 만든 문자열
MadeLetters=''
# index는 입력받은 숫자리스트 인덱스
def makeCombination(index, MadeLetters):
    # 백트래킹 부분
    # 가지치기
    # 입력된 숫자 index(길이)가 3글자가 된다면 추가
    if index == len(inputNumbers):
        result.append(MadeLetters)
        # return result
    # 아직 덜 됬다면
    else:
        # i는 입력받은 숫자
        i = inputNumbers[index]
        # chars는 입력된 숫자에 해당되는 문자열들
        chars = phoneNumber[i]
        for char in chars:
            makeCombination(index+1, MadeLetters + char)
    return result

print(makeCombination(0, MadeLetters))


