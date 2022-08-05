import sys
input = sys.stdin.readline

n = int(input())     #만날 아이들 + 거점지의 수

gift = []

for i in range(n):
    a = list(map(int, input().split()))
    if a[0] == 0:   #0이 입력됐다면 아이들을 만난것.
        if len(gift):    #줄 선물이 있으면
            print(max(gift))    #가장 가치가 큰 선물 줌
            gift.remove(max(gift))
        else:
            print('-1')
    else:           #거점에서 선물 리필
        for j in range(a.pop(0)):   #a첫번째 요소는 리필할 선물의 개수. 그만큼 for문 돌려줌
            gift.append(a.pop(0))   #gift에 선물 추가