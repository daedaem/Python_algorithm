import sys
sys.stdin =open('11654.txt')
word = input()
# print(word)
if word.isascii() == True:
    print(ord(word))
elif word.isdigit() == True:
    print(chr(int(word)))