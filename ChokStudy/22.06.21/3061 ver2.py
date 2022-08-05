num = []
goal = []
T = int(input())
k = 1
count = 0
for i in range(T):
    N = int(input())
    num = [j for j in range(N)]
    num = list(map(int,input().split()))
    goal = [l for l in range(1,N+1)]
    while goal != num:
        if num[k] < num[k-1]:
            num[k],num[k-1] = num[k-1],num[k]
            k += 1
            count += 1
        elif num[k] > num[k-1]:
            k += 1
        if k == N:
            k = 1
    print(count)
    count = 0
    k = 1