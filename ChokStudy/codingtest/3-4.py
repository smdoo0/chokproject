n, k = map(int, input().split())
cnt = 0

while 1:
    target = (n // k) * k
    cnt += n - target
    n = target
    if n < k:
        break
    else:
        n //= k
        cnt += 1

cnt += (n - 1)
print(cnt)