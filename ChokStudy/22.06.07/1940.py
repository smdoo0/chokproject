n = int(input())
m = int(input())
unq = list(map(int, input().split()))

armor = 0

for i in range(n):
    for j in range(n - i):
        if unq[i] + unq[i + j] == m:
            armor += 1

print(armor)                  #시간초과 뜸