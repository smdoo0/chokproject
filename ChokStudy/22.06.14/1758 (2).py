N = int(input())
tip = [int(input()) for _ in range(N)]
tip.sort(reverse= True)
for i in range(N):
    if tip[i]-i >= 0:
        tip[i] -= i
    else:
        tip[i] = 0
print(sum(tip))