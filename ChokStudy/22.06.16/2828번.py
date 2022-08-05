N, M = map(int, input().split())
j = int(input())

apple = [int(input()) for _ in range(j)]

move = 0 # 바구니가 얼마만큼 이동하는지

end = M  # 바구니의 오른쪽 끝 위치를 저장
start = 1  # 바구니의 왼쪽 끝 위치를 저장

for i in range(j):
    if (end >= apple[i] and start <= apple[i]): # 바구니가 사과를 받을 수 있는 위치인 경우
        continue
    elif (end < apple[i]): # 사과가 바구니의 오른쪽에서 떨어지는 경우
        move += apple[i] - end
        end = apple[i]
        start = apple[i] - (M - 1)
    elif (start > apple[i]): # 사과가 바구니의 왼쪽에서 떨어지는 경우
        move += start - apple[i]
        start = apple[i]
        end = apple[i] + (M - 1)

print(move)