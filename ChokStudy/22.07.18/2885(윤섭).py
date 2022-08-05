import sys
input = sys.stdin.readline
K = int(input())
D = 1
count = 0
while True:
    if K > D:
        D *= 2
    else:
        break
Temp = D
while K > 0:
    if K >= Temp: #2의 배수 조각
        K -= Temp #가장 큰 2의 배수 조각을 빼주는 것
    else:
        Temp //= 2 #반으로 쪼개고
        count += 1 #쪼갠 횟수 증가
print(D, count)
