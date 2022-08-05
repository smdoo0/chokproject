n = int(input())
wal = list(map(int, input().split()))

sum = 0

for i in range(n - 1):
    wal.sort(reverse=True)
    score = wal[0] * wal[1]
    slime = wal[0] + wal[1]
    sum += score

    wal.append(slime)
    wal.pop(0)
    wal.pop(0)

print(sum)