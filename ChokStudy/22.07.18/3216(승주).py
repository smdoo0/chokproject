#현재 조각의 노래가 재생되는동안 다음 조각 다운 가능
#현재 조각의 노래 길이와 다음 조각의 다운로드에 필요한 시간을 비교하여
# 1. 다음 조각의 다운로드 시간이 더 길다면
#   -->  둘의 차이만큼 다운로드 시간이 더 필요함. cnt에 차이 더해줌.
# 2. 현재 조각의 노래길이가 더 길다면
#   -->  둘의 차이만큼 다음 조각을 다운로드하는데에 여유가 생김. stack에 담았다가 다음 조각 재생시간에 더해줌.

import sys
input = sys.stdin.readline

n = int(input())        #노래 조각의 개수

d_v = [list(map(int, input().split())) for _ in range(n)]

#각 조각의 노래길이와 다운로드에 걸리는 시간
playing = 0         #현재 재생되는 조각의 노래길이
loading = 0         #다운로드에 필요한 시간
cnt = d_v[0][1]     #출력할 결과. 처음 조각의 다운로드 시간부터 시작.
stack = 0           #여유시간

for i in range(n - 1):
    loading = d_v[i+1][1]           #다음 조각 다운에 필요한 시간
    playing = d_v[i][0] + stack     #현재 재생되는 조각의 노래길이 + 이전 조각에서의 여유시간
    stack = 0                       #초기화
    if loading > playing:           #다음 조각 다운에 필요한 시간이 현재 재생되는 조각의 노래길이보다 길다면
        cnt += loading - playing    #그 차이만큼 결과에 더해줌
    else:                           #현재 재생되는 조각의 노래길이가 다음 조각 다운에 필요한 시간보다 길거나 같다면
        stack += playing - loading  #그 차이만큼 여유가 생김. stack에 담아줌

print(cnt)