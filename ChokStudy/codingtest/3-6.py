n = int(input())
p = list(map(int, input().split()))
p.sort()

g = []
cnt = 0
for i in range(n):
    g.append(p[i])
    if max(g) == len(g):
        cnt += 1
        g = []
    else:
        pass

print(cnt)