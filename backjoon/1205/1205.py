
import sys
sys.stdin =open('1205.txt')

#N은 랭킹리스트에 있는 점수 갯수
#P는 랭킹에 올라갈 수 있는 점수
#Song은 송유진 점수
# tc = int(input())
# for _ in range(1, tc+1):
N, Song, P = map(int, input().split())
# N이 0보다크면 계산,

if N > 0:
    rank_list = list(map(int, input().split()))
    # 랭킹 기록할 변수 rank_record
    # print(N, Song, P)
    # print(rank_list)

    # rank_list.sort()
    for i in range(1, len(rank_list)):
        for j in range(len(rank_list)-i):
            if rank_list[j]< rank_list[j+1]:
                rank_list[j], rank_list[j + 1] = rank_list[j+1], rank_list[j]
    # print(rank_list)
    # 일단 리스트에 넣자
    songlist = [Song, 1]
    rank_list.append(songlist)
    # print(rank_list)

    for i in range(N-1, -1, -1):
        if rank_list[i] < songlist[0]:
            rank_list.pop(rank_list.index(songlist))
            rank_list.insert(i, songlist)
    # print(rank_list)
        # else:
    # print(rank_list)
    rank = rank_list[:P]
    rank_record = [1] * (N+1)
    # 리스트에 있을 때
    # print(rank)
    if songlist not in rank:
        print(-1)
    else:
        rank[rank.index(songlist)] = songlist[0]
        for i in range(len(rank)-1): # 요부분 N으로 했다가 계속틀림
            if rank[i] > rank[i+1]:
                rank_record[i+1] = i+2
                # cnt = 1
            elif rank[i] == rank[i+1]:
                rank_record[i], rank_record[i+1] = rank.index(rank[i])+1, rank.index(rank[i])+1
        print(rank_record[rank.index(songlist[0])])
        # print(rank)
        # print(rank_record)
    #리스트에 없을 땐 -1
# N이 0이면 걍 바로 1등
if N == 0:
    print(1)

# 간단한 조건 첫번째로 두고 ~

# 패고 싶은 문제네...
# 반례  - N이 0인 case, N이 P보다 작은 case N보다 P가 큰 case,
# 반례 - 송유진 점수가 젤 큰 or 작은 경우 or 같은 경우 case