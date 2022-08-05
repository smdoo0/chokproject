n = int(input())

for i in range(n):
    data = list(map(int, input().split()))
    number = data.pop(0)
    data.sort()
    win = 0

    cnt = 1
    for i in range(number-1):
        if data[i] == data[i+1]:
            cnt+=1
            if cnt > number/2:
                win += 1
                print(data[i])
                break
        else:
            cnt = 1

    if win == 0:
        print('SYJKGW')