import math

# 에라토스테네스의 체
A, B, D = map(int, input().split())
li = [1]*(B+1)

for i in range(2, int(math.sqrt(B))+1):
    if li[i]:
        for j in range(i+i, B+1, i):
            li[j] = 0
so_su = [i for i in range(A, B+1) if li[i]]

cnt = 0
for n in so_su:
    if str(D) in str(n):
        cnt += 1
print(cnt)