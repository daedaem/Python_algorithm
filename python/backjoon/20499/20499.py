import sys
sys.stdin=open('20499.txt')

# k+a <d or d=0가짜 아니면 진짜
KDA = list(map(int,(input().split('/'))))
# print(KDA)
if KDA[0]+KDA[2] < KDA[1] or KDA[1] ==0:
    print("hasu")
else:
    print("gosu")