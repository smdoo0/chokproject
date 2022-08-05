import sys
input = sys.stdin.readline
n, k = map(int, input().split())
contry = [list(map(int, input().split())) for _ in range(n)]
contry.sort(key=lambda x : (-x[1], -x[2], -x[3])) # 금메달이 많은 순으로 정렬을 하고,
# 금메달이 같다면 은메달, 은메달이 같다면 동메달이 많은순으로
# 내림차순으로 정렬을 해준다.
for i in range(n):
    if contry[i][0] == k:
        index = i # 국가번호 index 찾음
for j in range(n):
    if contry[index][1:] == contry[j][1:]: # 메달이 많은 순으로 내림차순으로 정렬한 배열에서 국가번호 index를 찾음
        print(j + 1)
        break