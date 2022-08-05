N = int(input())          #로프의 개수

max = []                  #로프가 각각 들 수 있는 최대 중량

for i in range(N):
    x = int(input())
    max.append(x)                   #이거 리스트 내포 사용해서 만들수있나?

max.sort()                       #오름차순 정렬

summax = []                      #로프가 들 수 있는 모든 중량의 경우의 수
M = N

while M > 0 :
    summax.append(max[0] * M)
    M -= 1
    max.pop(0)

summax.sort()

print(summax[-1])