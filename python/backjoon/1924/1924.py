import sys
sys.stdin = open('1924.txt')
#7로 나눠서 나머지가 1이면 월요일 안남으면 일요일
workdaylist = list(range(7))
x, y = map(int, input().split())
# 1,1월요일 2.1 목 3.1 목 각 날짜 +1 2.28수 60 33 =1 수 61=0 75 32
daylist = [[], list(range(0, 32)), list(range(31, 60)),list(range(59, 91)), list(range(90, 121)), list(range(120, 152)),list(range(151, 182)), list(range(181, 213)), list(range(212, 244)), list(range(243, 274)), list(range(273, 305)),list(range(304, 335)), list(range(334, 366))]
if daylist[x][y]% 7 == 0:
    print('SUN')
if daylist[x][y]% 7 == 1:
    print('MON')
if daylist[x][y]% 7 == 2:
    print('TUE')
if daylist[x][y]% 7 == 3:
    print('WED')
if daylist[x][y]% 7 == 4:
    print('THU')
if daylist[x][y]% 7 == 5:
    print('FRI')
if daylist[x][y]% 7 == 6:
    print('SAT')